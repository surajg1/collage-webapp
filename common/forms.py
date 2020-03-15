# from django import forms
# from django.contrib.auth import (authenticate, get_user_model)

# User = get_user_model()

# class UserLoginForms(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget = forms.PasswordInput)
    
#     def clean(self, *args, **kwargs):
#         username = self.changed_data.get('username')
#         password = self.changed_data.get('password')
        
#         if username and password :
#             user = authenticate(username = username, password = password)
            
#             if not user:
#                 raise forms.ValidationError("This user is not avalablel!!")
            
#             if not user.check_password(password):
#                 raise forms.ValidationError("Password is incorrect!!")
            
#             if not user.is_active:
#                 raise forms.ValidationError("This user is not active!!")
            
#         return super(UserLoginForms, self).clean(**args, **kwargs)

# # class UserRegisterForm(forms.ModelForm):