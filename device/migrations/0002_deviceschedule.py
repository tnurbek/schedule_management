# Generated by Django 3.1.2 on 2020-11-28 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet1', models.CharField(default='-', max_length=128)),
                ('meet2', models.CharField(default='-', max_length=128)),
                ('meet3', models.CharField(default='-', max_length=128)),
                ('meet4', models.CharField(default='-', max_length=128)),
                ('meet5', models.CharField(default='-', max_length=128)),
                ('meet6', models.CharField(default='-', max_length=128)),
                ('meet7', models.CharField(default='-', max_length=128)),
                ('meet8', models.CharField(default='-', max_length=128)),
                ('meet9', models.CharField(default='-', max_length=128)),
                ('meet10', models.CharField(default='-', max_length=128)),
                ('meet11', models.CharField(default='-', max_length=128)),
                ('meet12', models.CharField(default='-', max_length=128)),
                ('meet13', models.CharField(default='-', max_length=128)),
                ('meet14', models.CharField(default='-', max_length=128)),
                ('meet15', models.CharField(default='-', max_length=128)),
                ('meet16', models.CharField(default='-', max_length=128)),
                ('meet17', models.CharField(default='-', max_length=128)),
                ('meet18', models.CharField(default='-', max_length=128)),
                ('meet19', models.CharField(default='-', max_length=128)),
                ('meet20', models.CharField(default='-', max_length=128)),
                ('meet21', models.CharField(default='-', max_length=128)),
                ('meet22', models.CharField(default='-', max_length=128)),
                ('meet23', models.CharField(default='-', max_length=128)),
                ('meet24', models.CharField(default='-', max_length=128)),
                ('meet25', models.CharField(default='-', max_length=128)),
                ('meet26', models.CharField(default='-', max_length=128)),
                ('meet27', models.CharField(default='-', max_length=128)),
                ('meet28', models.CharField(default='-', max_length=128)),
                ('meet29', models.CharField(default='-', max_length=128)),
                ('meet30', models.CharField(default='-', max_length=128)),
                ('meet31', models.CharField(default='-', max_length=128)),
                ('meet32', models.CharField(default='-', max_length=128)),
                ('meet33', models.CharField(default='-', max_length=128)),
                ('meet34', models.CharField(default='-', max_length=128)),
                ('meet35', models.CharField(default='-', max_length=128)),
                ('meet36', models.CharField(default='-', max_length=128)),
                ('meet37', models.CharField(default='-', max_length=128)),
                ('meet38', models.CharField(default='-', max_length=128)),
                ('meet39', models.CharField(default='-', max_length=128)),
                ('meet40', models.CharField(default='-', max_length=128)),
                ('meet41', models.CharField(default='-', max_length=128)),
                ('meet42', models.CharField(default='-', max_length=128)),
                ('meet43', models.CharField(default='-', max_length=128)),
                ('meet44', models.CharField(default='-', max_length=128)),
                ('meet45', models.CharField(default='-', max_length=128)),
                ('meet46', models.CharField(default='-', max_length=128)),
                ('meet47', models.CharField(default='-', max_length=128)),
                ('meet48', models.CharField(default='-', max_length=128)),
                ('meet49', models.CharField(default='-', max_length=128)),
                ('meet50', models.CharField(default='-', max_length=128)),
                ('meet51', models.CharField(default='-', max_length=128)),
                ('meet52', models.CharField(default='-', max_length=128)),
                ('meet53', models.CharField(default='-', max_length=128)),
                ('meet54', models.CharField(default='-', max_length=128)),
                ('meet55', models.CharField(default='-', max_length=128)),
                ('meet56', models.CharField(default='-', max_length=128)),
                ('meet57', models.CharField(default='-', max_length=128)),
                ('meet58', models.CharField(default='-', max_length=128)),
                ('meet59', models.CharField(default='-', max_length=128)),
                ('meet60', models.CharField(default='-', max_length=128)),
                ('meet61', models.CharField(default='-', max_length=128)),
                ('meet62', models.CharField(default='-', max_length=128)),
                ('meet63', models.CharField(default='-', max_length=128)),
                ('meet64', models.CharField(default='-', max_length=128)),
                ('meet65', models.CharField(default='-', max_length=128)),
                ('meet66', models.CharField(default='-', max_length=128)),
                ('meet67', models.CharField(default='-', max_length=128)),
                ('meet68', models.CharField(default='-', max_length=128)),
                ('meet69', models.CharField(default='-', max_length=128)),
                ('meet70', models.CharField(default='-', max_length=128)),
                ('meet71', models.CharField(default='-', max_length=128)),
                ('meet72', models.CharField(default='-', max_length=128)),
                ('meet73', models.CharField(default='-', max_length=128)),
                ('meet74', models.CharField(default='-', max_length=128)),
                ('meet75', models.CharField(default='-', max_length=128)),
                ('meet76', models.CharField(default='-', max_length=128)),
                ('meet77', models.CharField(default='-', max_length=128)),
                ('meet78', models.CharField(default='-', max_length=128)),
                ('meet79', models.CharField(default='-', max_length=128)),
                ('meet80', models.CharField(default='-', max_length=128)),
                ('meet81', models.CharField(default='-', max_length=128)),
                ('meet82', models.CharField(default='-', max_length=128)),
                ('meet83', models.CharField(default='-', max_length=128)),
                ('meet84', models.CharField(default='-', max_length=128)),
                ('meet85', models.CharField(default='-', max_length=128)),
                ('meet86', models.CharField(default='-', max_length=128)),
                ('meet87', models.CharField(default='-', max_length=128)),
                ('meet88', models.CharField(default='-', max_length=128)),
                ('meet89', models.CharField(default='-', max_length=128)),
                ('meet90', models.CharField(default='-', max_length=128)),
                ('meet91', models.CharField(default='-', max_length=128)),
                ('meet92', models.CharField(default='-', max_length=128)),
                ('meet93', models.CharField(default='-', max_length=128)),
                ('meet94', models.CharField(default='-', max_length=128)),
                ('meet95', models.CharField(default='-', max_length=128)),
                ('meet96', models.CharField(default='-', max_length=128)),
                ('meet97', models.CharField(default='-', max_length=128)),
                ('meet98', models.CharField(default='-', max_length=128)),
                ('meet99', models.CharField(default='-', max_length=128)),
                ('meet100', models.CharField(default='-', max_length=128)),
                ('meet101', models.CharField(default='-', max_length=128)),
                ('meet102', models.CharField(default='-', max_length=128)),
                ('meet103', models.CharField(default='-', max_length=128)),
                ('meet104', models.CharField(default='-', max_length=128)),
                ('meet105', models.CharField(default='-', max_length=128)),
                ('meet106', models.CharField(default='-', max_length=128)),
                ('meet107', models.CharField(default='-', max_length=128)),
                ('meet108', models.CharField(default='-', max_length=128)),
                ('meet109', models.CharField(default='-', max_length=128)),
                ('meet110', models.CharField(default='-', max_length=128)),
                ('meet111', models.CharField(default='-', max_length=128)),
                ('meet112', models.CharField(default='-', max_length=128)),
                ('meet113', models.CharField(default='-', max_length=128)),
                ('meet114', models.CharField(default='-', max_length=128)),
                ('meet115', models.CharField(default='-', max_length=128)),
                ('meet116', models.CharField(default='-', max_length=128)),
                ('meet117', models.CharField(default='-', max_length=128)),
                ('meet118', models.CharField(default='-', max_length=128)),
                ('meet119', models.CharField(default='-', max_length=128)),
                ('meet120', models.CharField(default='-', max_length=128)),
                ('meet121', models.CharField(default='-', max_length=128)),
                ('meet122', models.CharField(default='-', max_length=128)),
                ('meet123', models.CharField(default='-', max_length=128)),
                ('meet124', models.CharField(default='-', max_length=128)),
                ('meet125', models.CharField(default='-', max_length=128)),
                ('meet126', models.CharField(default='-', max_length=128)),
                ('meet127', models.CharField(default='-', max_length=128)),
                ('meet128', models.CharField(default='-', max_length=128)),
                ('meet129', models.CharField(default='-', max_length=128)),
                ('meet130', models.CharField(default='-', max_length=128)),
                ('meet131', models.CharField(default='-', max_length=128)),
                ('meet132', models.CharField(default='-', max_length=128)),
                ('meet133', models.CharField(default='-', max_length=128)),
                ('meet134', models.CharField(default='-', max_length=128)),
                ('meet135', models.CharField(default='-', max_length=128)),
                ('meet136', models.CharField(default='-', max_length=128)),
                ('meet137', models.CharField(default='-', max_length=128)),
                ('meet138', models.CharField(default='-', max_length=128)),
                ('meet139', models.CharField(default='-', max_length=128)),
                ('meet140', models.CharField(default='-', max_length=128)),
                ('meet141', models.CharField(default='-', max_length=128)),
                ('meet142', models.CharField(default='-', max_length=128)),
                ('meet143', models.CharField(default='-', max_length=128)),
                ('meet144', models.CharField(default='-', max_length=128)),
                ('meet145', models.CharField(default='-', max_length=128)),
                ('meet146', models.CharField(default='-', max_length=128)),
                ('meet147', models.CharField(default='-', max_length=128)),
                ('meet148', models.CharField(default='-', max_length=128)),
                ('meet149', models.CharField(default='-', max_length=128)),
                ('meet150', models.CharField(default='-', max_length=128)),
                ('meet151', models.CharField(default='-', max_length=128)),
                ('meet152', models.CharField(default='-', max_length=128)),
                ('meet153', models.CharField(default='-', max_length=128)),
                ('meet154', models.CharField(default='-', max_length=128)),
                ('meet155', models.CharField(default='-', max_length=128)),
                ('meet156', models.CharField(default='-', max_length=128)),
                ('meet157', models.CharField(default='-', max_length=128)),
                ('meet158', models.CharField(default='-', max_length=128)),
                ('meet159', models.CharField(default='-', max_length=128)),
                ('meet160', models.CharField(default='-', max_length=128)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.device')),
            ],
        ),
    ]
