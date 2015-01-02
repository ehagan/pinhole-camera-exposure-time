pinhole-camera-exposure-time
============================

Pinhole camera exposure time calculator.

I made this to compute exposure times for a pinhole camera I made, using my regular camera as a light meter.

Usage notes:
Set camera to spot metering, no exposure compensation.

In manual mode, set f-stop and ISO. I used f/2.8 ISO100 for a start.
Adjust shutter speed until something dark is at 0 on the exposure scale. We want to expose for the shadows because the pinhole camera is "film" (actually photographic print paper).

In Aperture Priority mode, set f-stop and ISO, point at something dark and half press the shutter or do whatever you have set to trigger metering. The camera tells you the target exposure time.

Now we have:
Meter f-stop
Meter ISO
Meter exposure time

The pinhole camera was built with an aperture made with a #10 sharp hand sewing needle.
http://www.jjneedles.com/products/Regular-Sharp-Hand-Sewing-Needles-Sizes-5%252d10.html
says that that makes the diameter about 0.53mm

We take that over to
http://www.mrpinhole.com/calcpinh.php
enter 6.36" focal length (20" half circumference / pi)
enter 0.53mm pinhole diameter
and get f/305
The pinhole could be as large as the next needle size up which is 0.61mm producing f/265

Our paper is Ilford Multigrade IV RC (5x7 for testing, final is planned to be 12.5 x 20) which the general internet estimates as ISO 6.

That gives us:
Pinhole f-stop
Pinhole ISO

Sample usage:
pinhole.py 2.8 294. 100.0 6.25 0.01

f scaling factor: 11025.0

ISO scaling factor: 16.0

unadjusted exposure time: 0:29:24.000

adjusted   exposure time: 4:50:39.917

In this example the camera says our exposure time should be 1/100th of a second. That's a nominal EV of 11. The unadjusted exposure time is about a half hour. The adjusted exposure time is almost five hours. The adjusted time here is likely quite wrong but the only equation I could find for the reciprocity breakdown adjustment of paper negatives was the one in the script.
