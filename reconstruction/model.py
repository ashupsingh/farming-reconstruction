"""New reconstruction, 2026-10-23. Demo inputs are synthetic, not historical results."""
import math
def validate_sample(sample,now):
    limits={'temperature_c':(-40,85),'humidity_percent':(0,100),'moisture_percent':(0,100)}
    errors=[]
    for field,(low,high) in limits.items():
        value=sample.get(field)
        if not isinstance(value,(int,float)) or not math.isfinite(value) or not low<=value<=high:errors.append(field)
    timestamp=sample.get('timestamp')
    stale=not isinstance(timestamp,(int,float)) or not math.isfinite(timestamp) or not 0<=now-timestamp<=30
    return {'valid':not errors and not stale,'invalid_fields':errors,'stale':stale,'source':sample.get('source','unspecified')}
def demo():
    s={'temperature_c':25,'humidity_percent':50,'moisture_percent':40,'timestamp':10,'source':'synthetic'}
    assert validate_sample(s,11)['valid'];assert validate_sample(s,50)['stale']
    s['humidity_percent']=150;assert not validate_sample(s,11)['valid']
    return {'invalid_and_stale_samples_rejected':True}

if __name__ == "__main__":
    import json
    print(json.dumps(demo(), indent=2))
