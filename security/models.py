from django.db import models
from django.utils.timezone import now

class Incident(models.Model):
    REPORT_TYPES = [
        ('Panic', 'Panic Alert'),
        ('CCTV', 'CCTV Alert'),
        ('Incident', 'Reported Incident'),
    ]
    report_type = models.CharField(max_length=20, choices=REPORT_TYPES)
    description = models.TextField()
    reported_at = models.DateTimeField(default=now)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.report_type} - {self.reported_at}"
