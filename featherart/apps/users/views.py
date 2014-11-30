from django.shortcuts import render_to_response
from users.forms import UserForm
from django.views.generic import CreateView
from django.contrib.auth.models import User


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserForm
    model = User
    success_url = '/users/success/'

    def form_valid(self, form):
        # Do things
        print "Form is valid."
        self.object = form.save()
        return render_to_response(
            'users/register_success.html',
            self.get_context_data(form=form)
        )

# def register(request):
#     context = RequestContext(request)

#     registered = False

#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)

#         if user_form.is_valid():
#             user = user_form.save()

#             user.set_password(user.password)
#             user.save()

#             registered = True
#         else:
#             print user_form.errors
#     else:
#         user_form = UserForm()

#     return render_to_response(
#         'users/register.html',
#         {'user_form': user_form, 'registered': registered},
#         context
#         )
