from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type

class AccountActivationTokenGenrator(PasswordResetTokenGenerator):
  def _make_hash(self,user,timestamp):
    return (
      text_type(user.pk) +text_type(timestamp)+
      text_type(user.is_active)
    )

account_activation_token = AccountActivationTokenGenrator()