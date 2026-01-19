from rest_framework.permissions import BasePermission



class IsOwner(BasePermission):
    ''' Can only be edited or deleted by the owner of the quiz.
    '''
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user