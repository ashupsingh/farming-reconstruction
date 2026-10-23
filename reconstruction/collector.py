"""Read JSON lines from stdin and record them locally; no simulated readings are injected."""
import json,sys,sqlite3,datetime,argparse
p=argparse.ArgumentParser();p.add_argument('--database',default='telemetry.sqlite');args=p.parse_args()
db=sqlite3.connect(args.database)
db.execute('CREATE TABLE IF NOT EXISTS readings(received_at TEXT NOT NULL,payload TEXT NOT NULL)')
try:
    for line in sys.stdin:
        try:
            row=json.loads(line)
            if not isinstance(row,dict) or row.get('source') not in ('hardware','synthetic'):raise ValueError('Missing source label')
            # JSON standards exclude nonfinite numeric values.
            payload=json.dumps(row,allow_nan=False)
            db.execute('INSERT INTO readings VALUES (?,?)',(datetime.datetime.now(datetime.timezone.utc).isoformat(),payload));db.commit()
        except (ValueError,TypeError) as e:print('Rejected input: '+str(e),file=sys.stderr)
finally:db.close()
