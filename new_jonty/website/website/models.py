# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models, connection

class AllPlayers(models.Model):
    player = models.TextField(db_column='Player', blank=True, null=True)  # Field name made lowercase.
    club = models.TextField(db_column='Club', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    player_id = models.BigIntegerField(db_column='Player ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    team_id = models.TextField(db_column='Team ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appearances = models.BigIntegerField(db_column='Appearances', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_players'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Table1(models.Model):
    year_player_id = models.BigIntegerField(primary_key=True)
    player_id = models.BigIntegerField(db_column='Player_ID', blank=True, null=True)  # Field name made lowercase.
    team_id = models.BigIntegerField(db_column='Team_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_1'


class Table2(models.Model):
    team_id = models.BigIntegerField(db_column='Team_ID', primary_key=True)  # Field name made lowercase.
    team = models.TextField(db_column='Team', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_2'


class Table3(models.Model):
    player_id = models.BigIntegerField(db_column='Player_ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table_3'

class FootballerQuery(models.Manager):
    def player_names(self, player1, player2):
        cursor = connection.cursor()
        cursor.execute("""
            select FirstSet.Name
            from
            (
            select Name from table_3
                where Player_ID in (
                    select Player_ID from table_1
                    where Team_ID in (
                        select Team_ID from table_1
                        where Player_ID in (
                            select Player_ID from table_3
                            where Name = %s)))) as FirstSet
                inner join 
                 (
            select Name from table_3
                where Player_ID in (
                    select Player_ID from table_1
                    where Team_ID in (
                        select Team_ID from table_1
                        where Player_ID in (
                            select Player_ID from table_3
                            where Name = %s)))) as SecondSet
                on FirstSet.Name = SecondSet.Name
                order by FirstSet.Name;""", [player1, player2])
        rows = cursor.fetchall()
        return [row[0] for row in rows] 
            
           
class Player(models.Model):
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    objects = FootballerQuery()
