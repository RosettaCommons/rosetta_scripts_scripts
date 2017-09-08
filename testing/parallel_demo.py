

from __future__ import print_function

import imp, json


parallel = imp.load_source('parallel', './../../tests/benchmark/util/parallel.py')


R  = parallel.Runner(5)

results = R.run_commands_lines('demo',
                              commands_lines = dict(line_a='ls', line_b='probably_an_error'),
                              working_dir = '.',
                              delete_intermediate_files = True
)

print( 'Run results: {}'.format( json.dumps(results, sort_keys=True, indent=2) ) )


''' Example output
% python parallel_demo.py
Running : probably_an_error
Running : ls
/bin/sh: probably_an_error: command not found
line_a 0 demo.line_b.output
parallel_demo.py
parse_all_scripts.py
validate_all_scripts.py
verify_all_scripts_accounted_for.py

line_b 127 /bin/sh: probably_an_error: command not found

Run results: {
  "line_a": {
    "output": "demo.line_b.output\nparallel_demo.py\nparse_all_scripts.py\nvalidate_all_scripts.py\nverify_all_scripts_accounted_for.py\n",
    "result": 0
  },
  "line_b": {
    "output": "/bin/sh: probably_an_error: command not found\n",
    "result": 127
  }
}
'''
