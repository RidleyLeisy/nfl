# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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


class Blocks(models.Model):
    pid = models.IntegerField(unique=True,primary_key=True)
    blk = models.CharField(max_length=7)
    brcv = models.CharField(max_length=7, blank=True, null=True)
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'blocks'


class Charts(models.Model):
    gid = models.IntegerField()
    pid = models.IntegerField(unique=True)
    detail = models.TextField()
    off = models.CharField(max_length=3)
    def_field = models.CharField(db_column='def', max_length=3)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=4)
    qb = models.CharField(max_length=7)
    trg = models.CharField(max_length=7, blank=True, null=True)
    qtr = models.IntegerField()
    los = models.CharField(max_length=6)
    dwn = models.IntegerField()
    ytg = models.IntegerField()
    yfog = models.IntegerField()
    zone = models.IntegerField()
    yds = models.CharField(max_length=3, blank=True, null=True)
    succ = models.IntegerField()
    fd = models.IntegerField()
    sg = models.IntegerField()
    nh = models.IntegerField()
    comp = models.IntegerField()
    ints = models.IntegerField()
    box = models.IntegerField()
    avt = models.IntegerField()
    pru = models.IntegerField()
    spru = models.IntegerField()
    blz = models.IntegerField()
    dblz = models.IntegerField()
    tts = models.IntegerField()
    pap = models.IntegerField()
    side = models.IntegerField()
    high = models.IntegerField()
    oop = models.IntegerField()
    shov = models.IntegerField()
    scr = models.IntegerField()
    qbp = models.IntegerField()
    qbhi = models.IntegerField()
    qbhu = models.IntegerField()
    htm = models.IntegerField()
    tay = models.IntegerField()
    dot = models.IntegerField()
    dotr = models.IntegerField()
    cov = models.IntegerField()
    cnb = models.IntegerField()
    crr = models.IntegerField()
    yac = models.IntegerField()
    drp = models.IntegerField()
    qbta = models.IntegerField()
    bap = models.IntegerField()
    intw = models.IntegerField()
    back = models.IntegerField()
    rb = models.IntegerField()
    te = models.IntegerField()
    def1 = models.CharField(max_length=7, blank=True, null=True)
    def2 = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'charts'


class College(models.Model):
    uid = models.IntegerField(unique=True)
    ncaa_id = models.IntegerField()
    player = models.CharField(max_length=7)
    class_field = models.IntegerField(db_column='class')  # Field renamed because it was a Python reserved word.
    col = models.CharField(max_length=35)
    pos = models.CharField(max_length=2)
    games = models.IntegerField()
    pc = models.CharField(max_length=3, blank=True, null=True)
    pa = models.CharField(max_length=3, blank=True, null=True)
    py = models.CharField(max_length=4, blank=True, null=True)
    tdp = models.CharField(max_length=2, blank=True, null=True)
    pint = models.CharField(max_length=2, blank=True, null=True)
    prat = models.CharField(max_length=6, blank=True, null=True)
    ra = models.CharField(max_length=3, blank=True, null=True)
    ry = models.CharField(max_length=4, blank=True, null=True)
    tdr = models.CharField(max_length=2, blank=True, null=True)
    rec = models.CharField(max_length=3, blank=True, null=True)
    tdrec = models.CharField(max_length=2, blank=True, null=True)
    recy = models.CharField(max_length=4, blank=True, null=True)
    solo = models.CharField(max_length=3, blank=True, null=True)
    comb = models.CharField(max_length=3, blank=True, null=True)
    tfloss = models.CharField(max_length=4, blank=True, null=True)
    sck = models.CharField(max_length=4, blank=True, null=True)
    ints = models.CharField(max_length=4, blank=True, null=True)
    iry = models.CharField(max_length=3, blank=True, null=True)
    tdint = models.CharField(max_length=2, blank=True, null=True)
    frcv = models.CharField(max_length=2, blank=True, null=True)
    fry = models.CharField(max_length=3, blank=True, null=True)
    tdfum = models.CharField(max_length=2, blank=True, null=True)
    forc = models.CharField(max_length=2, blank=True, null=True)
    pata = models.CharField(max_length=3, blank=True, null=True)
    patm = models.CharField(max_length=3, blank=True, null=True)
    fga = models.CharField(max_length=3, blank=True, null=True)
    fgm = models.CharField(max_length=3, blank=True, null=True)
    kpts = models.CharField(max_length=3, blank=True, null=True)
    pu = models.CharField(max_length=3, blank=True, null=True)
    puy = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'college'


class Conversions(models.Model):
    pid = models.IntegerField(unique=True)
    type = models.CharField(max_length=4)
    bc = models.CharField(max_length=7, blank=True, null=True)
    psr = models.CharField(max_length=7, blank=True, null=True)
    trg = models.CharField(max_length=7, blank=True, null=True)
    conv = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'conversions'


class Defense(models.Model):
    uid = models.IntegerField(unique=True)
    gid = models.IntegerField()
    player = models.CharField(max_length=7)
    solo = models.DecimalField(max_digits=3, decimal_places=1)
    comb = models.DecimalField(max_digits=3, decimal_places=1)
    sck = models.DecimalField(max_digits=2, decimal_places=1)
    saf = models.IntegerField()
    blk = models.IntegerField()
    ints = models.IntegerField()
    pdef = models.IntegerField()
    frcv = models.IntegerField()
    forc = models.IntegerField()
    tdd = models.IntegerField()
    rety = models.IntegerField()
    tdret = models.IntegerField()
    peny = models.IntegerField()
    snp = models.IntegerField()
    fp = models.DecimalField(max_digits=4, decimal_places=2)
    fp2 = models.DecimalField(max_digits=4, decimal_places=2)
    game = models.IntegerField()
    seas = models.IntegerField()
    year = models.IntegerField()
    team = models.CharField(max_length=3)
    posd = models.CharField(max_length=8)
    jnum = models.IntegerField()
    dcp = models.IntegerField()
    nflid = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'defense'


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


class Drives(models.Model):
    uid = models.IntegerField(unique=True)
    gid = models.IntegerField()
    fpid = models.IntegerField()
    tname = models.CharField(max_length=3)
    drvn = models.IntegerField()
    obt = models.CharField(max_length=4, blank=True, null=True)
    qtr = models.IntegerField()
    min = models.IntegerField()
    sec = models.IntegerField()
    yfog = models.IntegerField()
    plays = models.IntegerField()
    succ = models.IntegerField()
    rfd = models.IntegerField()
    pfd = models.IntegerField()
    ofd = models.IntegerField()
    ry = models.IntegerField()
    ra = models.IntegerField()
    py = models.IntegerField()
    pa = models.IntegerField()
    pc = models.IntegerField()
    peyf = models.IntegerField()
    peya = models.IntegerField()
    net = models.IntegerField()
    res = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drives'


class Fgxps(models.Model):
    pid = models.IntegerField(unique=True)
    fgxp = models.CharField(max_length=2)
    fkicker = models.CharField(max_length=7)
    dist = models.IntegerField()
    good = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fgxps'


class Fumbles(models.Model):
    pid = models.IntegerField(unique=True)
    fum = models.CharField(max_length=7)
    frcv = models.CharField(max_length=7, blank=True, null=True)
    fry = models.IntegerField()
    forc = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fumbles'


class Games(models.Model):
    gid = models.IntegerField(unique=True,primary_key=True)
    seas = models.IntegerField()
    wk = models.IntegerField()
    day = models.CharField(max_length=3)
    v = models.CharField(max_length=3)
    h = models.CharField(max_length=3)
    stad = models.CharField(max_length=45)
    temp = models.CharField(max_length=4, blank=True, null=True)
    humd = models.CharField(max_length=4, blank=True, null=True)
    wspd = models.CharField(max_length=4, blank=True, null=True)
    wdir = models.CharField(max_length=4, blank=True, null=True)
    cond = models.CharField(max_length=15, blank=True, null=True)
    surf = models.CharField(max_length=30)
    ou = models.DecimalField(max_digits=3, decimal_places=1)
    sprv = models.DecimalField(max_digits=3, decimal_places=1)
    ptsv = models.IntegerField()
    ptsh = models.IntegerField()
    
    class Meta:
        managed = False
        db_table = 'games'


class Injuries(models.Model):
    uid = models.IntegerField(unique=True)
    gid = models.IntegerField()
    player = models.CharField(max_length=7)
    team = models.CharField(max_length=3)
    details = models.CharField(max_length=25, blank=True, null=True)
    pstat = models.CharField(max_length=35, blank=True, null=True)
    gstat = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'injuries'


class Interceptions(models.Model):
    pid = models.IntegerField(unique=True)
    psr = models.CharField(max_length=7)
    ints = models.CharField(max_length=7)
    iry = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interceptions'


class Kickers(models.Model):
    uid = models.IntegerField(unique=True)
    gid = models.IntegerField()
    player = models.CharField(max_length=7)
    pat = models.IntegerField()
    fgs = models.IntegerField()
    fgm = models.IntegerField()
    fgl = models.IntegerField()
    fp = models.DecimalField(max_digits=3, decimal_places=1)
    game = models.IntegerField()
    seas = models.IntegerField()
    year = models.IntegerField()
    team = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'kickers'


class Kickoffs(models.Model):
    pid = models.IntegerField(unique=True)
    kicker = models.CharField(max_length=7)
    kgro = models.IntegerField()
    knet = models.IntegerField()
    ktb = models.IntegerField()
    kr = models.CharField(max_length=7, blank=True, null=True)
    kry = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kickoffs'


class Offense(models.Model):
    uid = models.IntegerField(unique=True,primary_key=True)
    gid = models.IntegerField()
    player = models.CharField(max_length=7)
    pa = models.IntegerField()
    pc = models.IntegerField()
    py = models.IntegerField()
    ints = models.IntegerField()
    tdp = models.IntegerField()
    ra = models.IntegerField()
    sra = models.IntegerField()
    ry = models.IntegerField()
    tdr = models.IntegerField()
    trg = models.IntegerField()
    rec = models.IntegerField()
    recy = models.IntegerField()
    tdrec = models.IntegerField()
    ret = models.IntegerField()
    rety = models.IntegerField()
    tdret = models.IntegerField()
    fuml = models.IntegerField()
    peny = models.IntegerField()
    conv = models.IntegerField()
    snp = models.IntegerField()
    fp = models.DecimalField(max_digits=4, decimal_places=2)
    fp2 = models.DecimalField(max_digits=4, decimal_places=2)
    fp3 = models.DecimalField(max_digits=4, decimal_places=2)
    game = models.IntegerField()
    seas = models.IntegerField()
    year = models.IntegerField()
    team = models.CharField(max_length=3)
    posd = models.CharField(max_length=8)
    jnum = models.IntegerField()
    dcp = models.IntegerField()
    nflid = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offense'


class Passing(models.Model):
    pid = models.IntegerField(unique=True, primary_key=True)
    psr = models.CharField(max_length=7)
    trg = models.CharField(max_length=7, blank=True, null=True)
    loc = models.CharField(max_length=2)
    yds = models.IntegerField()
    comp = models.IntegerField()
    succ = models.IntegerField()
    spk = models.IntegerField()
    dfb = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'passing'


class Penalties(models.Model):
    uid = models.IntegerField(unique=True)
    pid = models.IntegerField()
    ptm = models.CharField(max_length=3)
    pen = models.CharField(max_length=7, blank=True, null=True)
    desc = models.CharField(max_length=40)
    cat = models.IntegerField()
    pey = models.IntegerField()
    act = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'penalties'


class Player(models.Model):
    player = models.CharField(unique=True, max_length=7,primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=25)
    pname = models.CharField(max_length=25)
    pos1 = models.CharField(max_length=2)
    pos2 = models.CharField(max_length=2, blank=True, null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    dob = models.CharField(max_length=10, blank=True, null=True)
    forty = models.DecimalField(max_digits=3, decimal_places=2)
    bench = models.IntegerField()
    vertical = models.DecimalField(max_digits=3, decimal_places=1)
    broad = models.IntegerField()
    shuttle = models.DecimalField(max_digits=3, decimal_places=2)
    cone = models.DecimalField(max_digits=3, decimal_places=2)
    arm = models.DecimalField(max_digits=5, decimal_places=3)
    hand = models.DecimalField(max_digits=5, decimal_places=3)
    dpos = models.IntegerField()
    col = models.CharField(max_length=35)
    dv = models.CharField(max_length=35, blank=True, null=True)
    start = models.IntegerField()
    cteam = models.CharField(max_length=3)
    posd = models.CharField(max_length=8)
    jnum = models.IntegerField()
    dcp = models.IntegerField()
    nflid = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlaysFlat(models.Model):
    gid = models.IntegerField(primary_key=True)
    pid = models.IntegerField(unique=True)
    detail = models.TextField()
    off = models.CharField(max_length=3)
    def_field = models.CharField(db_column='def', max_length=3)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=4)
    dseq = models.IntegerField()
    len = models.IntegerField()
    qtr = models.IntegerField()
    min = models.IntegerField()
    sec = models.IntegerField()
    ptso = models.IntegerField()
    ptsd = models.IntegerField()
    timo = models.IntegerField()
    timd = models.IntegerField()
    dwn = models.CharField(max_length=1, blank=True, null=True)
    ytg = models.CharField(max_length=2, blank=True, null=True)
    yfog = models.CharField(max_length=2, blank=True, null=True)
    zone = models.CharField(max_length=1, blank=True, null=True)
    yds = models.CharField(max_length=3, blank=True, null=True)
    succ = models.CharField(max_length=1, blank=True, null=True)
    fd = models.CharField(max_length=1, blank=True, null=True)
    sg = models.CharField(max_length=1, blank=True, null=True)
    nh = models.CharField(max_length=1, blank=True, null=True)
    pts = models.CharField(max_length=2, blank=True, null=True)
    bc = models.CharField(max_length=7, blank=True, null=True)
    kne = models.CharField(max_length=1, blank=True, null=True)
    dir = models.CharField(max_length=2, blank=True, null=True)
    rtck1 = models.CharField(max_length=7, blank=True, null=True)
    rtck2 = models.CharField(max_length=7, blank=True, null=True)
    psr = models.CharField(max_length=7, blank=True, null=True)
    comp = models.CharField(max_length=1, blank=True, null=True)
    spk = models.CharField(max_length=1, blank=True, null=True)
    loc = models.CharField(max_length=2, blank=True, null=True)
    trg = models.CharField(max_length=7, blank=True, null=True)
    dfb = models.CharField(max_length=7, blank=True, null=True)
    ptck1 = models.CharField(max_length=7, blank=True, null=True)
    ptck2 = models.CharField(max_length=7, blank=True, null=True)
    sk1 = models.CharField(max_length=7, blank=True, null=True)
    sk2 = models.CharField(max_length=7, blank=True, null=True)
    ptm1 = models.CharField(max_length=3, blank=True, null=True)
    pen1 = models.CharField(max_length=7, blank=True, null=True)
    desc1 = models.CharField(max_length=40, blank=True, null=True)
    cat1 = models.CharField(max_length=1, blank=True, null=True)
    pey1 = models.CharField(max_length=2, blank=True, null=True)
    act1 = models.CharField(max_length=1, blank=True, null=True)
    ptm2 = models.CharField(max_length=3, blank=True, null=True)
    pen2 = models.CharField(max_length=7, blank=True, null=True)
    desc2 = models.CharField(max_length=40, blank=True, null=True)
    cat2 = models.CharField(max_length=1, blank=True, null=True)
    pey2 = models.CharField(max_length=2, blank=True, null=True)
    act2 = models.CharField(max_length=1, blank=True, null=True)
    ptm3 = models.CharField(max_length=3, blank=True, null=True)
    pen3 = models.CharField(max_length=7, blank=True, null=True)
    desc3 = models.CharField(max_length=40, blank=True, null=True)
    cat3 = models.CharField(max_length=1, blank=True, null=True)
    pey3 = models.CharField(max_length=2, blank=True, null=True)
    act3 = models.CharField(max_length=1, blank=True, null=True)
    ints = models.CharField(max_length=7, blank=True, null=True)
    iry = models.CharField(max_length=3, blank=True, null=True)
    fum = models.CharField(max_length=7, blank=True, null=True)
    frcv = models.CharField(max_length=7, blank=True, null=True)
    fry = models.CharField(max_length=3, blank=True, null=True)
    forc = models.CharField(max_length=7, blank=True, null=True)
    saf = models.CharField(max_length=7, blank=True, null=True)
    blk = models.CharField(max_length=7, blank=True, null=True)
    brcv = models.CharField(max_length=7, blank=True, null=True)
    fgxp = models.CharField(max_length=2, blank=True, null=True)
    fkicker = models.CharField(max_length=7, blank=True, null=True)
    dist = models.CharField(max_length=2, blank=True, null=True)
    good = models.CharField(max_length=1, blank=True, null=True)
    punter = models.CharField(max_length=7, blank=True, null=True)
    pgro = models.CharField(max_length=3, blank=True, null=True)
    pnet = models.CharField(max_length=3, blank=True, null=True)
    ptb = models.CharField(max_length=1, blank=True, null=True)
    pr = models.CharField(max_length=7, blank=True, null=True)
    pry = models.CharField(max_length=3, blank=True, null=True)
    pfc = models.CharField(max_length=1, blank=True, null=True)
    kicker = models.CharField(max_length=7, blank=True, null=True)
    kgro = models.CharField(max_length=3, blank=True, null=True)
    knet = models.CharField(max_length=3, blank=True, null=True)
    ktb = models.CharField(max_length=1, blank=True, null=True)
    kr = models.CharField(max_length=7, blank=True, null=True)
    kry = models.CharField(max_length=3, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'plays_flat'


class Punts(models.Model):
    pid = models.IntegerField(unique=True)
    punter = models.CharField(max_length=7)
    pgro = models.IntegerField()
    pnet = models.IntegerField()
    ptb = models.IntegerField()
    pr = models.CharField(max_length=7, blank=True, null=True)
    pry = models.IntegerField()
    pfc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'punts'


class Redzone(models.Model):
    uid = models.IntegerField(unique=True)
    gid = models.IntegerField()
    player = models.CharField(max_length=7)
    pa = models.IntegerField()
    pc = models.IntegerField()
    py = models.IntegerField()
    ints = models.IntegerField()
    ra = models.IntegerField()
    sra = models.IntegerField()
    ry = models.IntegerField()
    trg = models.IntegerField()
    rec = models.IntegerField()
    recy = models.IntegerField()
    fuml = models.IntegerField()
    peny = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'redzone'


class Rushing(models.Model):
    pid = models.IntegerField(unique=True)
    bc = models.CharField(max_length=7)
    dir = models.CharField(max_length=2)
    yds = models.IntegerField()
    succ = models.IntegerField()
    kne = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rushing'


class Sacks(models.Model):
    uid = models.IntegerField(unique=True)
    pid = models.IntegerField()
    qb = models.CharField(max_length=7)
    sk = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=2, decimal_places=1)
    ydsl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sacks'


class Safeties(models.Model):
    pid = models.IntegerField(unique=True)
    saf = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'safeties'


class Schedule(models.Model):
    gid = models.IntegerField(unique=True)
    seas = models.IntegerField()
    wk = models.IntegerField()
    day = models.CharField(max_length=3)
    date = models.TextField()
    v = models.CharField(max_length=3)
    h = models.CharField(max_length=3)
    stad = models.CharField(max_length=45)
    surf = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'schedule'


class Tackles(models.Model):
    uid = models.IntegerField(unique=True)
    pid = models.IntegerField()
    tck = models.CharField(max_length=7)
    value = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'tackles'


class Teams(models.Model):
    tid = models.IntegerField(primary_key=True)
    gid = models.IntegerField()
    tname = models.CharField(max_length=3)
    pts = models.IntegerField()
    q1p = models.IntegerField()
    q2p = models.IntegerField()
    q3p = models.IntegerField()
    q4p = models.IntegerField()
    rfd = models.IntegerField()
    pfd = models.IntegerField()
    ifd = models.IntegerField()
    ry = models.IntegerField()
    ra = models.IntegerField()
    py = models.IntegerField()
    pa = models.IntegerField()
    pc = models.IntegerField()
    sk = models.IntegerField()
    ints = models.IntegerField()
    fum = models.IntegerField()
    pu = models.IntegerField()
    gpy = models.IntegerField()
    pr = models.IntegerField()
    pry = models.IntegerField()
    kr = models.IntegerField()
    kry = models.IntegerField()
    ir = models.IntegerField()
    iry = models.IntegerField()
    pen = models.IntegerField()
    top = models.DecimalField(max_digits=3, decimal_places=1)
    td = models.IntegerField()
    tdr = models.IntegerField()
    tdp = models.IntegerField()
    tdt = models.IntegerField()
    fgm = models.IntegerField()
    fgat = models.IntegerField()
    fgy = models.IntegerField()
    rza = models.IntegerField()
    rzc = models.IntegerField()
    bry = models.IntegerField()
    bpy = models.IntegerField()
    srp = models.IntegerField()
    s1rp = models.IntegerField()
    s2rp = models.IntegerField()
    s3rp = models.IntegerField()
    spp = models.IntegerField()
    s1pp = models.IntegerField()
    s2pp = models.IntegerField()
    s3pp = models.IntegerField()
    lea = models.IntegerField()
    ley = models.IntegerField()
    lta = models.IntegerField()
    lty = models.IntegerField()
    lga = models.IntegerField()
    lgy = models.IntegerField()
    mda = models.IntegerField()
    mdy = models.IntegerField()
    rga = models.IntegerField()
    rgy = models.IntegerField()
    rta = models.IntegerField()
    rty = models.IntegerField()
    rea = models.IntegerField()
    rey = models.IntegerField()
    r1a = models.IntegerField()
    r1y = models.IntegerField()
    r2a = models.IntegerField()
    r2y = models.IntegerField()
    r3a = models.IntegerField()
    r3y = models.IntegerField()
    qba = models.IntegerField()
    qby = models.IntegerField()
    sla = models.IntegerField()
    sly = models.IntegerField()
    sma = models.IntegerField()
    smy = models.IntegerField()
    sra = models.IntegerField()
    sry = models.IntegerField()
    dla = models.IntegerField()
    dly = models.IntegerField()
    dma = models.IntegerField()
    dmy = models.IntegerField()
    dra = models.IntegerField()
    dry = models.IntegerField()
    wr1a = models.IntegerField()
    wr1y = models.IntegerField()
    wr3a = models.IntegerField()
    wr3y = models.IntegerField()
    tea = models.IntegerField()
    tey = models.IntegerField()
    rba = models.IntegerField()
    rby = models.IntegerField()
    sga = models.IntegerField()
    sgy = models.IntegerField()
    p1a = models.IntegerField()
    p1y = models.IntegerField()
    p2a = models.IntegerField()
    p2y = models.IntegerField()
    p3a = models.IntegerField()
    p3y = models.IntegerField()
    spc = models.IntegerField()
    mpc = models.IntegerField()
    lpc = models.IntegerField()
    q1ra = models.IntegerField()
    q1ry = models.IntegerField()
    q1pa = models.IntegerField()
    q1py = models.IntegerField()
    lcra = models.IntegerField()
    lcry = models.IntegerField()
    lcpa = models.IntegerField()
    lcpy = models.IntegerField()
    rzra = models.IntegerField()
    rzry = models.IntegerField()
    rzpa = models.IntegerField()
    rzpy = models.IntegerField()
    sky = models.IntegerField()
    lbs = models.DecimalField(max_digits=3, decimal_places=1)
    dbs = models.DecimalField(max_digits=3, decimal_places=1)
    sfpy = models.IntegerField()
    drv = models.IntegerField()
    npy = models.IntegerField()
    tb = models.IntegerField()
    i20 = models.IntegerField()
    rtd = models.IntegerField()
    lnr = models.DecimalField(max_digits=3, decimal_places=1)
    lnp = models.DecimalField(max_digits=3, decimal_places=1)
    lbr = models.DecimalField(max_digits=3, decimal_places=1)
    lbp = models.DecimalField(max_digits=3, decimal_places=1)
    dbr = models.DecimalField(max_digits=3, decimal_places=1)
    dbp = models.DecimalField(max_digits=3, decimal_places=1)
    nha = models.IntegerField()
    s3a = models.IntegerField()
    s3c = models.IntegerField()
    l3a = models.IntegerField()
    l3c = models.IntegerField()
    stf = models.IntegerField()
    dp = models.IntegerField()
    fsp = models.IntegerField()
    ohp = models.IntegerField()
    pbep = models.IntegerField()
    dlp = models.IntegerField()
    dsp = models.IntegerField()
    dum = models.IntegerField()
    pfn = models.IntegerField()
    snpo = models.IntegerField()
    snpd = models.IntegerField()
    saf = models.IntegerField()
    blk = models.IntegerField()
    fp = models.IntegerField()
    box4 = models.IntegerField()
    box4y = models.IntegerField()
    box5 = models.IntegerField()
    box5y = models.IntegerField()
    box6 = models.IntegerField()
    box6y = models.IntegerField()
    box7 = models.IntegerField()
    box7y = models.IntegerField()
    box8 = models.IntegerField()
    box8y = models.IntegerField()
    avt1 = models.IntegerField()
    avt1y = models.IntegerField()
    avt2 = models.IntegerField()
    avt2y = models.IntegerField()
    avt3 = models.IntegerField()
    avt3y = models.IntegerField()
    avt4 = models.IntegerField()
    avt4y = models.IntegerField()
    avt5 = models.IntegerField()
    avt5y = models.IntegerField()
    pru3 = models.IntegerField()
    pru3y = models.IntegerField()
    pru4 = models.IntegerField()
    pru4y = models.IntegerField()
    pru5 = models.IntegerField()
    pru5y = models.IntegerField()
    spru1 = models.IntegerField()
    spru1y = models.IntegerField()
    spru2 = models.IntegerField()
    spru2y = models.IntegerField()
    scrm = models.IntegerField()
    scrmy = models.IntegerField()
    blz0 = models.IntegerField()
    blz0y = models.IntegerField()
    blz1 = models.IntegerField()
    blz1y = models.IntegerField()
    blz2 = models.IntegerField()
    blz2y = models.IntegerField()
    dblz1 = models.IntegerField()
    dblz1y = models.IntegerField()
    tts = models.IntegerField()
    pap = models.IntegerField()
    papy = models.IntegerField()
    side = models.IntegerField()
    sidey = models.IntegerField()
    high = models.IntegerField()
    highy = models.IntegerField()
    oop = models.IntegerField()
    oopy = models.IntegerField()
    shov = models.IntegerField()
    shovy = models.IntegerField()
    scr = models.IntegerField()
    scry = models.IntegerField()
    npr = models.IntegerField()
    npry = models.IntegerField()
    qbp = models.IntegerField()
    qbpy = models.IntegerField()
    qbhi = models.IntegerField()
    qbhiy = models.IntegerField()
    qbhu = models.IntegerField()
    qbhuy = models.IntegerField()
    htm = models.IntegerField()
    htmy = models.IntegerField()
    ytg1 = models.IntegerField()
    ytg2 = models.IntegerField()
    ytg3 = models.IntegerField()
    tay1 = models.IntegerField()
    tay2 = models.IntegerField()
    tay3 = models.IntegerField()
    dot1 = models.IntegerField()
    dot2 = models.IntegerField()
    dot3 = models.IntegerField()
    dotr1 = models.IntegerField()
    dotr1y = models.IntegerField()
    dotr2 = models.IntegerField()
    dotr2y = models.IntegerField()
    dotr3 = models.IntegerField()
    dotr3y = models.IntegerField()
    dotr4 = models.IntegerField()
    dotr4y = models.IntegerField()
    cov0 = models.IntegerField()
    cov0y = models.IntegerField()
    cov1 = models.IntegerField()
    cov1y = models.IntegerField()
    cov2 = models.IntegerField()
    cov2y = models.IntegerField()
    cnb = models.IntegerField()
    cnbc = models.IntegerField()
    crr = models.IntegerField()
    crry = models.IntegerField()
    yac1 = models.IntegerField()
    yac2 = models.IntegerField()
    yac3 = models.IntegerField()
    drp = models.IntegerField()
    qbta = models.IntegerField()
    bap = models.IntegerField()
    intw = models.IntegerField()
    intwi = models.IntegerField()
    back0 = models.IntegerField()
    back0y = models.IntegerField()
    back1 = models.IntegerField()
    back1y = models.IntegerField()
    back2 = models.IntegerField()
    back2y = models.IntegerField()
    back3 = models.IntegerField()
    back3y = models.IntegerField()
    per11 = models.IntegerField()
    per11y = models.IntegerField()
    per12 = models.IntegerField()
    per12y = models.IntegerField()
    per21 = models.IntegerField()
    per21y = models.IntegerField()
    per22 = models.IntegerField()
    per22y = models.IntegerField()
    per13 = models.IntegerField()
    per13y = models.IntegerField()
    per10 = models.IntegerField()
    per10y = models.IntegerField()
    pc1 = models.IntegerField()
    pc2 = models.IntegerField()
    pc3 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teams'


class TempClass(models.Model):
    gid = models.IntegerField()
    pid = models.IntegerField(primary_key=True)
    detail = models.TextField()
    off = models.CharField(max_length=3)
    def_field = models.CharField(db_column='def', max_length=3)  # Field renamed because it was a Python reserved word.
    type = models.CharField(max_length=4)
    dseq = models.IntegerField()
    len = models.IntegerField()
    qtr = models.IntegerField()
    min = models.IntegerField()
    sec = models.IntegerField()
    ptso = models.IntegerField()
    ptsd = models.IntegerField()
    timo = models.IntegerField()
    timd = models.IntegerField()
    dwn = models.CharField(max_length=1, blank=True, null=True)
    ytg = models.CharField(max_length=2, blank=True, null=True)
    yfog = models.CharField(max_length=2, blank=True, null=True)
    zone = models.CharField(max_length=1, blank=True, null=True)
    yds = models.CharField(max_length=3, blank=True, null=True)
    succ = models.CharField(max_length=1, blank=True, null=True)
    fd = models.CharField(max_length=1, blank=True, null=True)
    sg = models.CharField(max_length=1, blank=True, null=True)
    nh = models.CharField(max_length=1, blank=True, null=True)
    pts = models.CharField(max_length=2, blank=True, null=True)
    bc = models.CharField(max_length=7, blank=True, null=True)
    kne = models.CharField(max_length=1, blank=True, null=True)
    dir = models.CharField(max_length=2, blank=True, null=True)
    rtck1 = models.CharField(max_length=7, blank=True, null=True)
    rtck2 = models.CharField(max_length=7, blank=True, null=True)
    psr = models.CharField(max_length=7, blank=True, null=True)
    comp = models.CharField(max_length=1, blank=True, null=True)
    spk = models.CharField(max_length=1, blank=True, null=True)
    loc = models.CharField(max_length=2, blank=True, null=True)
    trg = models.CharField(max_length=7, blank=True, null=True)
    dfb = models.CharField(max_length=7, blank=True, null=True)
    ptck1 = models.CharField(max_length=7, blank=True, null=True)
    ptck2 = models.CharField(max_length=7, blank=True, null=True)
    sk1 = models.CharField(max_length=7, blank=True, null=True)
    sk2 = models.CharField(max_length=7, blank=True, null=True)
    ptm1 = models.CharField(max_length=3, blank=True, null=True)
    pen1 = models.CharField(max_length=7, blank=True, null=True)
    desc1 = models.CharField(max_length=40, blank=True, null=True)
    cat1 = models.CharField(max_length=1, blank=True, null=True)
    pey1 = models.CharField(max_length=2, blank=True, null=True)
    act1 = models.CharField(max_length=1, blank=True, null=True)
    ptm2 = models.CharField(max_length=3, blank=True, null=True)
    pen2 = models.CharField(max_length=7, blank=True, null=True)
    desc2 = models.CharField(max_length=40, blank=True, null=True)
    cat2 = models.CharField(max_length=1, blank=True, null=True)
    pey2 = models.CharField(max_length=2, blank=True, null=True)
    act2 = models.CharField(max_length=1, blank=True, null=True)
    ptm3 = models.CharField(max_length=3, blank=True, null=True)
    pen3 = models.CharField(max_length=7, blank=True, null=True)
    desc3 = models.CharField(max_length=40, blank=True, null=True)
    cat3 = models.CharField(max_length=1, blank=True, null=True)
    pey3 = models.CharField(max_length=2, blank=True, null=True)
    act3 = models.CharField(max_length=1, blank=True, null=True)
    ints = models.CharField(max_length=7, blank=True, null=True)
    iry = models.CharField(max_length=3, blank=True, null=True)
    fum = models.CharField(max_length=7, blank=True, null=True)
    frcv = models.CharField(max_length=7, blank=True, null=True)
    fry = models.CharField(max_length=3, blank=True, null=True)
    forc = models.CharField(max_length=7, blank=True, null=True)
    saf = models.CharField(max_length=7, blank=True, null=True)
    blk = models.CharField(max_length=7, blank=True, null=True)
    brcv = models.CharField(max_length=7, blank=True, null=True)
    fgxp = models.CharField(max_length=2, blank=True, null=True)
    fkicker = models.CharField(max_length=7, blank=True, null=True)
    dist = models.CharField(max_length=2, blank=True, null=True)
    good = models.CharField(max_length=1, blank=True, null=True)
    punter = models.CharField(max_length=7, blank=True, null=True)
    pgro = models.CharField(max_length=3, blank=True, null=True)
    pnet = models.CharField(max_length=3, blank=True, null=True)
    ptb = models.CharField(max_length=1, blank=True, null=True)
    pr = models.CharField(max_length=7, blank=True, null=True)
    pry = models.CharField(max_length=3, blank=True, null=True)
    pfc = models.CharField(max_length=1, blank=True, null=True)
    kicker = models.CharField(max_length=7, blank=True, null=True)
    kgro = models.CharField(max_length=3, blank=True, null=True)
    knet = models.CharField(max_length=3, blank=True, null=True)
    ktb = models.CharField(max_length=1, blank=True, null=True)
    kr = models.CharField(max_length=7, blank=True, null=True)
    kry = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_class'


class Touchdowns(models.Model):
    pid = models.IntegerField(unique=True, primary_key=True)
    qtr = models.IntegerField()
    min = models.IntegerField()
    sec = models.IntegerField()
    dwn = models.IntegerField()
    yds = models.IntegerField()
    pts = models.IntegerField()
    player = models.CharField(max_length=7, blank=True, null=True)
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'touchdowns'


class Twitter(models.Model):
    tid = models.IntegerField()
    handle = models.CharField(max_length=15)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    player = models.CharField(max_length=7)
    created = models.TextField()
    tweet = models.TextField()
    source = models.CharField(max_length=40)
    fav = models.IntegerField()
    rt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'twitter'
