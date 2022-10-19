from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

#Imported from rallyApp.views multiple times to reduce line length
from rallyApp.views import home_page, post_detail, like_post, contact_page, register, login_func 
from rallyApp.views import profile_page, edit_profile, delete_profile, logout_func, follow_page
from rallyApp.views import change_password, forget_password, delete_comment, update_comment
from rallyApp.views import manage_posts, add_post, edit_post, delete_post


class TestRallyAppUrls(SimpleTestCase):

    def test_home_page_url_is_resolved(self):

        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page)

    def test_post_detail_url_is_resolved(self):

        url = reverse('post_detail', args=['example-slug'])
        self.assertEquals(resolve(url).func, post_detail)
