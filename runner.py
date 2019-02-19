import subprocess


pytest_run_arr = ['py.test', f'tests', '-vv', '-l',
        '--html=reports/report.html', '--self-contained-html','--driver', 'Chrome']

tests_proc = subprocess.run(pytest_run_arr)

if tests_proc.returncode != 0:
    raise Exception('Some tests is failed.')
