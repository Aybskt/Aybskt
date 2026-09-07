from pathlib import Path
import subprocess, json, os, sys, struct, zlib
root=Path(__file__).resolve().parents[1]
work=root/'.git/demo-run'
work.mkdir(exist_ok=True)
meta=Path(sys.argv[1]).resolve()
checker=Path(sys.argv[2]).resolve()
mc=work/'metadata-classes'; cc=work/'checker-classes'
mc.mkdir(exist_ok=True); cc.mkdir(exist_ok=True)
subprocess.run(['javac','-encoding','UTF-8','-cp',str(meta/'JAR Files/app.jar'),'-d',str(mc),*[str(p) for p in (meta/'src').rglob('*.java')]],check=True,capture_output=True)
cs=[p for p in (checker/'src').rglob('*.java') if 'GuiMod' not in p.parts and p.name!='module-info.java']
subprocess.run(['javac','-encoding','UTF-8','-d',str(cc),*[str(p) for p in cs]],check=True,capture_output=True)
def chunk(kind,data):
    return struct.pack('!I',len(data))+kind+data+struct.pack('!I',zlib.crc32(kind+data)&0xffffffff)
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('!2I5B',64,64,8,2,0,0,0))+chunk(b'IDAT',zlib.compress((b'\0'+bytes([30,65,42])*64)*64))+chunk(b'IEND',b'')
(work/'image.png').write_bytes(png)
(work/'sample.py').write_text('def greet(name):\n    return "Hello " + name\n\ndef square(value: int) -> int:\n    return value * value\n',encoding='utf-8')
records={}
def run(kind,args,label):
    command=['java','-Dfile.encoding=UTF-8','-cp',str(mc)+os.pathsep+str(meta/'JAR Files/app.jar'),'com.projectd10.App'] if kind=='metadata' else ['java','-Dfile.encoding=UTF-8','-cp',str(cc),'CliMod.Cli']
    r=subprocess.run(command+args,cwd=work,capture_output=True,text=True,encoding='utf-8',check=True)
    records.setdefault(kind,[]).append({'command':label,'stdout':r.stdout.replace(str(work),'[demo]').strip(),'stderr':r.stderr.strip()})
    return r.stdout
run('metadata',['-s','image.png','Code Secure Repeat','encoded.png'],'App -s image.png "Code Secure Repeat" encoded.png')
out=run('metadata',['-e','encoded.png'],'App -e encoded.png')
assert out.strip()=='Code Secure Repeat'
run('checker',['-f','sample.py','--type'],'Cli -f sample.py --type')
run('checker',['-f','sample.py','--sbutf8'],'Cli -f sample.py --sbutf8')
run('checker',['-f','sample.py','--head'],'Cli -f sample.py --head')
assert (work/'sample.py').read_text().startswith('#!/usr/bin/python3\n# -*- coding: utf-8 -*-\n')
for name,repo in [('metadata',meta),('checker',checker)]:
    records[name+'_commit']=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()
(root/'data/demo-transcripts.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(records,ensure_ascii=True,indent=2))
