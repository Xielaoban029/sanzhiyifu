const fs = require('fs');
const c = fs.readFileSync('index.html','utf8');
const start = c.lastIndexOf('<script>');
const end = c.lastIndexOf('</script>');
const js = c.slice(start + 8, end);
try {
  new Function(js);
  console.log('JS SYNTAX OK');
} catch(e) {
  console.log('ERROR:', e.message.slice(0,200));
  const m = e.stack.match(/:(\d+):(\d+)/);
  if (m) {
    const lines = js.split('\n');
    console.log('Line', m[1]);
    const ln = parseInt(m[1]) - 1;
    for (let j = Math.max(0,ln-2); j < Math.min(lines.length, ln+3); j++) {
      console.log(j+1, ':', lines[j].slice(0,120));
    }
  }
}
