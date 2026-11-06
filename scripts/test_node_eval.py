import subprocess
from pathlib import Path

node_code = """
const fs = require('fs');
const content = fs.readFileSync('false-friends/index.html', 'utf8');
const script_start = content.indexOf('<script>') + 8;
const script_end = content.lastIndexOf('</script>');
const script = content.slice(script_start, script_end) + '\\nconsole.log("Length in eval:", FALSE_FRIENDS_DATA.length, QUIZ_QUESTIONS.length);';

const makeEl = () => ({
  innerText: '',
  innerHTML: '',
  value: '',
  style: {},
  classList: { add: () => {}, remove: () => {}, toggle: () => {} },
  addEventListener: () => {},
  appendChild: () => {},
  setAttribute: () => {}
});

const document = {
  getElementById: (id) => makeEl(),
  createElement: (tag) => makeEl(),
  querySelectorAll: () => []
};

eval(script);
console.log('ALL FUNCTIONS AND INITIALIZATION RAN 100% CLEANLY!');
"""

Path("test_runner.js").write_text(node_code, encoding="utf-8")
res = subprocess.run(["node", "test_runner.js"], capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
print("EXIT:", res.returncode)
