from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class expert(models.Model):
    expert = models.ForeignKey(User , on_delete=models.CASCADE)
    is_expert = models.BooleanField(default=False)
    def __str__(self):
        return self.expert.username



class users(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    # expert = models.ForeignKey(expert,default=User, on_delete=models.CASCADE)
    order = models.BooleanField(default=False)

from django.db.models.signals import post_save , pre_save
def GroupSignal(sender , instance , **kwargs):
    # from django.contrib.auth.models import User
    from django.contrib.auth.models import Group
    from .views import expert_permissions
    user = instance.expert.id
    usere = instance.expert
    isexpert = instance.is_expert
    if isexpert == True:
        usere.is_staff = True
        usere.save()
        print(usere)
        expert_group = Group.objects.get(name='expert-group')
        expert_group.permissions.set(expert_permissions)
        expert_group.user_set.add(user)
        print("done!")
post_save.connect(GroupSignal , sender=expert)
