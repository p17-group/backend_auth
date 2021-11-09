from auth_example.models.account import Account
from auth_example.models.user    import User
from rest_framework              import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['balance', 'last_change_date', 'is_active']

    def to_representation(self, obj):
        account = Account.objects.get(id=obj.id)
        user    = User.objects.get(id=obj.user_id)
        return {
            'id':             account.id,
            'balance':        account.balance,
            'lastChangeDate': account.last_change_date,
            'isActive':       account.is_active,
            'user' : {
                'id':    user.id,
                'name':  user.name,
                'email': user.email,
            }
        }
