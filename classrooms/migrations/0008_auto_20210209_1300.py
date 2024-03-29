# Generated by Django 3.1.4 on 2021-02-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0007_auto_20210209_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='iframe',
        ),
        migrations.AddField(
            model_name='platform',
            name='domain',
            field=models.URLField(default='https://meet.jit.si/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platform',
            name='paramiters',
            field=models.CharField(default='#jitsi_meet_external_api_id=0&amp;config.requireDisplayName=true&amp;config.startAudioMuted=6&amp;config.disableAudioLevels=true&amp;interfaceConfig.DISABLE_VIDEO_BACKGROUND=true&interfaceConfig.SHOW_CHROME_EXTENSION_BANNER=false&config.disableDeepLinking=true&setVideoQuality=720', max_length=1000),
            preserve_default=False,
        ),
    ]
