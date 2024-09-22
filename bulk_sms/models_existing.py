# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountVerification(models.Model):
    account_verification_id = models.AutoField(primary_key=True)
    account = models.ForeignKey('Accounts', models.DO_NOTHING, blank=True, null=True)
    response = models.TextField()
    id_number = models.CharField(max_length=128)
    status = models.CharField(max_length=128)
    image = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_verification'


class Accounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    account_number = models.CharField(max_length=255)
    balance = models.FloatField(blank=True, null=True)
    balance_before = models.FloatField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


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
    first_name = models.CharField(max_length=150)
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


class CustomerCategories(models.Model):
    customer_category_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_categories'


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    shop = models.ForeignKey('Shops', models.DO_NOTHING, blank=True, null=True)
    customer_category_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


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


class Migrations(models.Model):
    id_migration = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    statements = models.TextField(blank=True, null=True)
    rollback_statements = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'migrations'


class NewsletterCustomers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newsletter_customers'


class OnboardBusinessdetails(models.Model):
    businessdetailid = models.AutoField(db_column='businessDetailId', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=200, blank=True, null=True)  # Field name made lowercase.
    businessregistrationnumber = models.CharField(db_column='businessRegistrationNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    natureofbusiness = models.CharField(db_column='natureOfBusiness', max_length=200, blank=True, null=True)  # Field name made lowercase.
    streetaddress = models.CharField(db_column='streetAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    postaladdress = models.CharField(db_column='postalAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alternatephonenumber = models.CharField(db_column='alternatePhoneNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField()
    created_by = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    updated_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    certofcorporation = models.CharField(db_column='certOfCorporation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    commencebusinesscert = models.CharField(db_column='commenceBusinessCert', max_length=100, blank=True, null=True)  # Field name made lowercase.
    companyprofilecert = models.CharField(db_column='companyProfileCert', max_length=100, blank=True, null=True)  # Field name made lowercase.
    numberofdirectors = models.IntegerField(db_column='numberOfDirectors')  # Field name made lowercase.
    useridfile = models.CharField(db_column='userIdFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    officialphonenumber = models.CharField(db_column='officialPhoneNumber', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'onboard_businessdetails'


class OnboardDirectorids(models.Model):
    directoridsid = models.AutoField(db_column='directorIdsId', primary_key=True)  # Field name made lowercase.
    directorids = models.CharField(db_column='directorIds', max_length=100, blank=True, null=True)  # Field name made lowercase.
    businessdetailid = models.ForeignKey(OnboardBusinessdetails, models.DO_NOTHING, db_column='businessDetailId_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'onboard_directorids'


class Shops(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100, blank=True, null=True)
    shop_description = models.CharField(max_length=255, blank=True, null=True)
    shop_assistant_name = models.CharField(max_length=100, blank=True, null=True)
    shop_assistant_number = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shops'


class UserOtps(models.Model):
    user_otp_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    status = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_generated = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_otps'


class UserTypes(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    user_type_name = models.CharField(max_length=255)
    user_type_description = models.CharField(max_length=255)
    active = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_types'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=40, blank=True, null=True)
    image_path = models.CharField(max_length=200, blank=True, null=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10)
    dob = models.DateTimeField()
    address = models.CharField(max_length=255, blank=True, null=True)
    id_type = models.CharField(max_length=5, blank=True, null=True)
    id_number = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=20, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    is_verified = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
