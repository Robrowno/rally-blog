from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve

# Imported from rallyApp.views multiple times to reduce line length
from rallyApp.views import (
    home_page, post_detail, like_post, contact_page, register, login_func
    )
from rallyApp.views import (
    profile_page, edit_profile, delete_profile, logout_func, follow_page
    )
from rallyApp.views import (
    change_password, forget_password, delete_comment, update_comment
    )
from rallyApp.views import (
    manage_posts, add_post, edit_post, delete_post
    )

# Testing NOT complete - all URLs pass, continue refactoring where appropriate


class TestRallyAppUrls(SimpleTestCase):
    """
    For testing the resolution of the urls in the rallyApp.
    """

    def test_home_page_url_is_resolved(self):

        """
        For testing the resolution of the home page url
        """

        url = reverse('home')
        self.assertEquals(resolve(url).func, home_page)

    def test_post_detail_url_is_resolved(self):

        """
        For testing the resolution of the post detail page url
        """

        url = reverse('post_detail', args=['example-slug'])
        self.assertEquals(resolve(url).func, post_detail)

    def test_like_post_url_is_resolved(self):

        """
        For testing the resolution of the like url
        """

        url = reverse('like_post', args=['example-slug'])
        self.assertEquals(resolve(url).func, like_post)

    def test_contact_page_url_is_resolved(self):

        """
        For testing the resolution of the contact page url
        """

        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact_page)

    def test_register_page_url_is_resolved(self):

        """
        For testing the resolution of the register page url
        """

        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_login_page_url_is_resolved(self):

        """
        For testing the resolution of the login page url
        """

        url = reverse('login')
        self.assertEquals(resolve(url).func, login_func)

    def test_profile_page_url_is_resolved(self):

        """
        For testing the resolution of the profile page url
        """

        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile_page)

    def test_edit_profile_page_url_is_resolved(self):

        """
        For testing the resolution of the edit profile url
        """

        url = reverse('edit_profile')
        self.assertEquals(resolve(url).func, edit_profile)

    def test_delete_profile_page_url_is_resolved(self):

        """
        For testing the resolution of the delete profile (account) url
        """

        url = reverse('delete_profile')
        self.assertEquals(resolve(url).func, delete_profile)

    def test_follow_page_url_is_resolved(self):

        """
        For testing the resolution of the follow page url
        """

        url = reverse('follow')
        self.assertEquals(resolve(url).func, follow_page)

    def test_logout_func_url_is_resolved(self):

        """
        For testing the resolution of the logout function url
        """

        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout_func)

    def test_change_password_url_is_resolved(self):

        """
        For testing the resolution of the password change url
        """
        id_x = int()

        url = reverse('change_password', args=[id_x])
        self.assertEquals(resolve(url).func, change_password)

    def test_forget_password_url_is_resolved(self):

        """
        For testing the resolution of the forget password url
        """

        url = reverse('forget_password')
        self.assertEquals(resolve(url).func, forget_password)

    def test_delete_comment_url_is_resolved(self):

        """
        For testing the resolution of the delete comment url
        """

        id_x = int()

        url = reverse('delete_comment', args=[id_x])
        self.assertEquals(resolve(url).func, delete_comment)

    def test_update_comment_url_is_resolved(self):

        """
        For testing the resolution of the update comment url
        """

        id_x = int()

        url = reverse('update_comment', args=[id_x])
        self.assertEquals(resolve(url).func, update_comment)

    def test_manage_posts_url_is_resolved(self):

        """
        For testing the resolution of the manage posts page url
        """

        url = reverse('manage')
        self.assertEquals(resolve(url).func, manage_posts)

    def test_add_posts_url_is_resolved(self):

        """
        For testing the resolution of the add post url
        """

        url = reverse('add')
        self.assertEquals(resolve(url).func, add_post)

    def test_edit_posts_url_is_resolved(self):

        """
        For testing the resolution of the edit post page url
        """
        id_x = int()

        url = reverse('edit', args=[id_x])
        self.assertEquals(resolve(url).func, edit_post)

    def test_delete_posts_url_is_resolved(self):

        """
        For testing the resolution of the delete post url
        """
        id_x = int()

        url = reverse('delete_post', args=[id_x])
        self.assertEquals(resolve(url).func, delete_post)
