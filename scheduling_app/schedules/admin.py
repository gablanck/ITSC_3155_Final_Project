from django.contrib import admin
from .models import (
    Event, 
    ConnectionRequest, 
    Connection,
    UserProfile,
    Notification,
    Comment,
    SharedSchedule,
    Group,
    GroupMembership,
    GroupInvitation
)

# Customize UserProfile admin display
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email', 'get_date_joined')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('user__date_joined',)
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    
    def get_date_joined(self, obj):
        return obj.user.date_joined
    get_date_joined.short_description = 'Date Joined'

# Customize Event admin display
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'start_time', 'end_time', 'category', 'is_recurring')
    list_filter = ('date', 'category', 'is_recurring', 'user')
    search_fields = ('title', 'description', 'user__username')
    date_hierarchy = 'date'

# Customize Connection admin display
@admin.register(Connection)
class ConnectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'connected_to', 'share_schedule', 'created_at')
    search_fields = ('user__username', 'connected_to__username')
    list_filter = ('created_at', 'share_schedule')

# Customize ConnectionRequest admin display
@admin.register(ConnectionRequest)
class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'accepted', 'created_at')
    list_filter = ('accepted', 'created_at')
    search_fields = ('sender__username', 'receiver__username')

# Customize Notification admin display
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('user__username', 'message')

# Customize Comment admin display
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'event__title', 'content')

# Customize Group admin display
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'created_at')
    search_fields = ('name', 'creator__username')
    list_filter = ('created_at',)

# Register remaining models with default admin
admin.site.register(SharedSchedule)
admin.site.register(GroupMembership)
admin.site.register(GroupInvitation)
