from rest_framework import serializers
from .models import Availability, Booking

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        overlapping = Booking.objects.filter(
            date=data['date'],
            start_time__lt=data['end_time'],
            end_time__gt=data['start_time']
        )
        if overlapping.exists():
            raise serializers.ValidationError("Time slot overlaps with existing booking.")
        return data
