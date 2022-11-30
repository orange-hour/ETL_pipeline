from django.contrib.auth.hashers import make_password

from rest_framework                  import status
from rest_framework.test             import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models  import User
from board.models import Blog


class TestBoard(APITestCase):
    '''
        자유게시판 TEST Code
    '''
    # Test시작전 필요한 임시 데이터 생성
    def setUp(self):
        self.user = User.objects.create(
            id       = 1,
            email    = "aaa@gmail.com",
            gender   = 'M',
            birth_date = '2000-01-01',
            nickname = "wanted",
            name     = "aaa",
            password = make_password("123"),
            is_active = True,
            is_admin = False  # 일반유저
            )
        self.user1 = User.objects.create(
            id       = 2,
            email    = "bbb@gmail.com",
            gender   = 'F',
            birth_date = '2000-02-01',
            nickname = "wanted2",
            name     = "bbb",
            password = make_password("123"),
            is_active = True,
            is_admin = False  # 일반유저
            )    
        self.board = Blog.objects.create(
            id      = 1,
            user_id = 1,
            title   = "게시판 제목 1",
            body = "게시판 내용 1"
        )
        self.board_url = "/blog/"

    # Test를 위해 생성했던 임시 데이터 삭제
    def tearDown(self):
        User.objects.all().delete()
        Blog.objects.all().delete()


    # 게시판 리스트 조회(로그인 했을경우)
    def test_board_list_login_success(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        
        self.response = self.client.get(self.board_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
    

    # 게시판 리스트 조회(로그인 안했을경우)
    def test_board_list_success(self):
        self.response = self.client.get(self.board_url, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


    # 자유게시판 상세페이지 조회(로그인했을경우)
    def test_board_detail_signin_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.get(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 상세페이지 조회(로그인안했을경우) - TEST FAIL (response == 301)
    def test_board_detail_signin_success(self):

        self.response = self.client.get(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 작성(로그인했을경우)
    def test_board_create_login_success(self):
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "게시판 추가 제목 2",
            "body": "게시판 추가 내용 2"
        }

        self.response = self.client.post(self.board_url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    # 자유게시판 글 작성 실패(로그인 안했을경우)
    def test_board_create_fail(self):
        data = {
            "title"  : "게시판 추가 제목 2",
            "body": "게시판 추가 내용 2"
        }

        self.response = self.client.post(self.board_url, data, format='json')
        
        self.assertEqual(self.response.status_code, status.HTTP_401_UNAUTHORIZED)

    # 자유게시판 글 업데이트성공(본인의 글인 경우) - TEST FAIL
    def test_board_update_login_success(self):
        
        self.refresh = RefreshToken.for_user(self.user)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title"  : "게시판 추가 제목 2",
            "body": "게시판 추가 내용 2"
        }

        self.response = self.client.put(f'{self.board_url}{self.board.id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    # 자유게시판 글 업데이트실패(본인글이 아닌 경우) - TEST FAIL (PUT method 없음)
    def test_notice_update_success(self):
        self.refresh = RefreshToken.for_user(self.user1)

        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        data = {
            "title": "공지사항 제목1 수정",
            "body": "공지사항 내용1수정",
        }

        self.response = self.client.put(f'{self.board_url}{self.board.id}', data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."})

    # 자유게시판 작성글 삭제(본인글인경우) - TEST FAIL (DELETE method 없음)
    def test_board_delete_success(self): 
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')
        
        self.response = self.client.delete(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    # 자유게시판 작성글 삭제(본인글이 아닌경우) - TEST FAIL (DELETE method 없음)
    def test_board_delete_fail(self):
        self.refresh = RefreshToken.for_user(self.user1)
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.refresh.access_token}')

        self.response = self.client.delete(f'{self.board_url}{self.board.id}', format='json')
        self.assertEqual(self.response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.json(), {'detail': "[Access Denied: ERR02] 작성자 외 게시글 수정, 삭제 권한이 없습니다."})