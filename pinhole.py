#!/usr/bin/python
import sys
import math

def adj(t):
    # Equation for reciprocity correction from
    # http://www.f295.org/main/showthread.php?14750-Ilford-MGIV-RC-Paper-Speed&s=cd1ba90df452bc871f9d0018bb384b6e&p=96052&viewfull=1#post96052
    return t + (0.0009 * (t ** 2.2304))

def exposure(f_meter, f_pinhole, iso_meter, iso_pinhole, exp_meter, adjust=False):
    scale_factor = (f_pinhole / f_meter)**2.0
    iso_factor = iso_meter / iso_pinhole
    print "f scaling factor: %s" % scale_factor
    print "ISO scaling factor: %s" % iso_factor
    return exp_meter * scale_factor * iso_factor

def time_string(sec):
    m, s = divmod(sec, 60.0)
    h, m = divmod(m, 60)
    return "%d:%02d:%06.3f" % (h, m, s)

def main():
    exposure_time = exposure(
        float(sys.argv[1]),  # Meter f stop
        float(sys.argv[2]),  # Pinhole f stop
        float(sys.argv[3]),  # Meter ISO
        float(sys.argv[4]),  # Pinhole ISO
        float(sys.argv[5]),  # Meter reported exposure time
    )

    print "unadjusted exposure time: %s" % time_string(exposure_time)
    print "adjusted   exposure time: %s" % time_string(adj(exposure_time))

if __name__ == '__main__':
    main()
