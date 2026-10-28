import os, re, random, string, time, json
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from flask import Flask, jsonify, make_response, request, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-before-public-use")
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", SESSION_COOKIE_SECURE=True)
HTML = r'''<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#090d1b"><title>Long Gmail 10ph</title>
<style>
:root{color-scheme:dark;--bg:#090d1b;--line:#263653;--muted:#95a4c2;--text:#f4f7ff;--cyan:#53e4ef;--purple:#9a83ff;--green:#5df0ad;--red:#ff718d}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(ellipse at 10% 0%,#182c4e 0,transparent 45%),radial-gradient(ellipse at 100% 35%,#241849 0,transparent 35%),var(--bg);font-family:system-ui,-apple-system,Roboto,"Segoe UI",sans-serif;color:var(--text);min-height:100vh}
.wrap{max-width:620px;margin:auto;padding:20px 15px 34px}.top{display:flex;align-items:center;gap:13px;margin:6px 0 23px}.logo{width:49px;height:49px;border-radius:16px;background:linear-gradient(135deg,var(--cyan),var(--purple));display:grid;place-items:center;color:#091122;font-weight:950;font-size:21px;box-shadow:0 8px 30px #53e4ef30}.brand{font-weight:850;letter-spacing:.7px;font-size:19px}.sub{font-size:12px;color:var(--muted);margin-top:2px;letter-spacing:1.5px}.pill{margin-left:auto;border:1px solid #29594e;color:var(--green);background:#102b2a;padding:6px 10px;border-radius:99px;font-size:11px;font-weight:750}
.hero{padding:22px;border:1px solid #304362;border-radius:25px;background:linear-gradient(140deg,#182842ee,#17152fee);box-shadow:0 16px 45px #0003;position:relative;overflow:hidden}.hero:after{content:"";position:absolute;width:180px;height:180px;border-radius:50%;background:#5ce5ef0d;right:-70px;top:-70px}.eyebrow{color:var(--muted);font-size:12px;font-weight:750;letter-spacing:1.7px}.email{font-size:clamp(17px,4.4vw,23px);font-weight:850;overflow-wrap:anywhere;margin:12px 0 17px;color:#70f3c0;line-height:1.4}.actions{display:grid;grid-template-columns:1fr 1fr;gap:10px}.btn{border:0;border-radius:14px;padding:13px 12px;font-weight:800;font-size:14px;cursor:pointer;transition:transform .12s,opacity .12s}.btn:active{transform:scale(.98)}.primary{background:linear-gradient(110deg,var(--cyan),#91f2d1);color:#071522}.secondary{background:#202d48;color:#eaf0ff;border:1px solid #344664}.timerbox{margin-top:22px;display:flex;justify-content:space-between;align-items:center;gap:12px}.timerlabel{font-size:12px;color:var(--muted);font-weight:700}.timer{font-size:28px;font-weight:900;font-variant-numeric:tabular-nums;letter-spacing:1px}.track{height:6px;border-radius:99px;background:#27334c;overflow:hidden;margin-top:11px}.progress{height:100%;width:100%;background:linear-gradient(90deg,var(--cyan),var(--purple));border-radius:99px;transition:width .4s}
.section{margin-top:16px;padding:19px;border:1px solid var(--line);border-radius:22px;background:#11192aee}.secthead{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px}.secttitle{font-size:16px;font-weight:850}.mini{font-size:11px;color:var(--muted)}.codebox{border-radius:16px;background:#0a1221;border:1px dashed #354866;padding:18px 14px;text-align:center;min-height:87px;display:grid;place-items:center}.code{font-size:28px;font-weight:900;letter-spacing:4px;color:var(--cyan);overflow-wrap:anywhere}.empty{color:#91a0bc;font-size:13px}.status{font-size:12px;color:var(--muted);display:flex;gap:8px;align-items:center;margin-top:13px}.dot{width:8px;height:8px;border-radius:50%;background:var(--green);box-shadow:0 0 10px #5df0ad80}.stats{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}.stat{background:#0c1424;border-radius:14px;padding:12px}.statlabel{font-size:11px;color:var(--muted)}.statval{font-size:19px;font-weight:850;margin-top:3px}.mailitem{padding:13px 0;border-bottom:1px solid #253149}.mailitem:last-child{border-bottom:0}.mailtitle{font-weight:750;font-size:14px;overflow-wrap:anywhere}.mailmeta{color:var(--muted);font-size:11px;margin-top:5px}.mailintro{font-size:12px;color:var(--muted);line-height:1.5}.footer{text-align:center;color:#71809d;font-size:11px;padding:20px 8px 0;line-height:1.7}.toast{position:fixed;left:50%;bottom:25px;transform:translate(-50%,20px);opacity:0;pointer-events:none;background:#e7fff7;color:#071b18;padding:12px 18px;border-radius:99px;font-size:13px;font-weight:800;box-shadow:0 10px 30px #0006;transition:.25s;max-width:90%;white-space:nowrap}.toast.show{opacity:1;transform:translate(-50%,0)}button:disabled{opacity:.5}
@media(min-width:540px){.wrap{padding-top:28px}.hero{padding:27px}.section{padding:22px}}
</style></head><body><main class="wrap">
<header class="top"><div class="logo">L</div><div><div class="brand">LONG GMAIL <span style="color:var(--cyan)">10PH</span></div><div class="sub">TEMP MAIL · ANDROID EDITION</div></div><div class="pill">● ĐANG CHẠY</div></header>
<section class="hero"><div class="eyebrow">EMAIL TẠM HIỆN TẠI</div><div class="email" id="email">Đang tạo email…</div><div class="actions"><button class="btn primary" id="copy">▣ &nbsp; Sao chép email</button><button class="btn secondary" id="rotate">↻ &nbsp; Đổi email ngay</button></div>
<div class="timerbox"><div><div class="timerlabel">TỰ ĐỘNG ĐỔI EMAIL SAU</div><div class="timer" id="timer">10:00</div></div><div style="text-align:right"><div class="timerlabel">KIỂM TRA THƯ</div><div style="font-size:15px;font-weight:800;margin-top:5px">Mỗi 1 giây</div></div></div><div class="track"><div class="progress" id="progress"></div></div></section>
<section class="section"><div class="secthead"><div class="secttitle">✦ Mã xác minh mới nhất</div><div class="mini" id="codeTime">ĐANG CHỜ</div></div><div class="codebox"><div id="code" class="empty">Chưa thấy mã trong thư mới.</div></div><div class="status"><span class="dot" id="dot"></span><span id="status">Đang kết nối dịch vụ email tạm…</span></div><div class="stats"><div class="stat"><div class="statlabel">THƯ TRONG HỘP THƯ</div><div class="statval" id="count">0</div></div><div class="stat"><div class="statlabel">DỊCH VỤ</div><div class="statval" style="font-size:16px">Mail.tm</div></div></div></section>
<section class="section"><div class="secthead"><div class="secttitle">▤ Hộp thư đến</div><button class="btn secondary" style="padding:8px 11px;font-size:12px" id="refresh">Làm mới ↻</button></div><div id="messages"><div class="mailintro">Email mới sẽ xuất hiện tại đây. Giữ trang này mở để tự kiểm tra thư.</div></div></section>
<div class="footer">Long Gmail 10ph · Mỗi trình duyệt có hộp thư riêng<br>Email tạm 1secmail, không phải tài khoản Google/Gmail thật.<br>Enter: đổi email ngay · Giữ trang mở để tự kiểm tra.</div></main><div class="toast" id="toast"></div>
<script>
const $=id=>document.getElementById(id);let deadline=Date.now()+600000,busy=false;
function toast(s){$('toast').textContent=s;$('toast').classList.add('show');setTimeout(()=>$('toast').classList.remove('show'),2100)}
async function api(path,method='GET'){let r=await fetch(path,{method,headers:{'Content-Type':'application/json'}});let j=await r.json();if(!r.ok||j.error)throw Error(j.error||'Có lỗi kết nối');return j}
async function rotate(){if(busy)return;busy=true;$('rotate').disabled=true;$('status').textContent='Đang tạo email mới…';try{let d=await api('/api/new','POST');$('email').textContent=d.email;deadline=Date.now()+600000;$('code').className='empty';$('code').textContent='Chưa thấy mã trong thư mới.';$('codeTime').textContent='ĐANG CHỜ';$('messages').innerHTML='<div class="mailintro">Đang chờ thư gửi đến địa chỉ mới…</div>';$('count').textContent='0';$('status').textContent='Email mới đã sẵn sàng';toast('Đã tạo email mới')}catch(e){$('status').textContent=e.message;toast(e.message)}finally{busy=false;$('rotate').disabled=false}}
async function poll(){if(busy)return;try{let d=await api('/api/messages');$('status').textContent=d.status||'Đã kiểm tra hộp thư';$('dot').style.background='var(--green)';$('count').textContent=d.messages.length;let html='';if(!d.messages.length)html='<div class="mailintro">Chưa có thư. Hộp thư đang tự kiểm tra mỗi giây.</div>';for(const m of d.messages){html+=`<div class="mailitem"><div class="mailtitle">${esc(m.subject||'(Không có tiêu đề)')}</div><div class="mailmeta">Từ: ${esc(m.from||'Không rõ')} · ${esc(m.createdAt||'')}</div>${m.code?`<div style="color:var(--cyan);font-weight:900;margin-top:7px">Mã: ${esc(m.code)}</div>`:''}</div>`}$('messages').innerHTML=html;if(d.messages.length){let found=d.messages.find(m=>m.code);if(found){$('code').className='code';$('code').textContent=found.code;$('codeTime').textContent='ĐÃ TÌM THẤY'}else if(!$('code').classList.contains('code')){$('code').className='empty';$('code').textContent='Có thư mới nhưng chưa nhận diện được mã.'}}}catch(e){$('status').textContent='Tạm lỗi kiểm tra: '+e.message;$('dot').style.background='var(--red)'}}
function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
$('copy').onclick=async()=>{try{await navigator.clipboard.writeText($('email').textContent);toast('Đã sao chép email')}catch(e){let t=document.createElement('textarea');t.value=$('email').textContent;document.body.appendChild(t);t.select();document.execCommand('copy');t.remove();toast('Đã sao chép email')}};
$('rotate').onclick=rotate;$('refresh').onclick=poll;document.addEventListener('keydown',e=>{if(e.key==='Enter'&&!['TEXTAREA','INPUT'].includes(document.activeElement.tagName)){e.preventDefault();rotate()}});
setInterval(()=>{let left=Math.max(0,deadline-Date.now()),sec=Math.ceil(left/1000);$('timer').textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');$('progress').style.width=(left/600000*100)+'%';if(left===0&&!busy)rotate()},250);
(async()=>{await rotate();await poll();setInterval(poll,1000)})();
</script></body></html>'''

def request_json(url):
    req = Request(url, headers={"Accept":"application/json", "User-Agent":"LongGmail10ph/1.0"})
    try:
        with urlopen(req, timeout=12) as r:
            raw=r.read().decode("utf-8", "replace")
            return json.loads(raw) if raw else {}
    except (HTTPError, URLError, TimeoutError) as e:
        raise RuntimeError("Dịch vụ email tạm đang lỗi hoặc không truy cập được: " + str(e))

def new_mail():
    # Each visitor gets a random mailbox. 1secmail does not guarantee custom Gmail addresses.
    login = "long" + "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    domain = "1secmail.com"
    session["mail_login"] = login
    session["mail_domain"] = domain
    session["mail_created"] = time.time()
    session.modified = True
    return login + "@" + domain

def get_messages():
    login=session.get("mail_login"); domain=session.get("mail_domain")
    if not login or not domain:
        return []
    data=request_json("https://www.1secmail.com/api/v1/?"+urlencode({"action":"getMessages","login":login,"domain":domain}))
    if not isinstance(data,list):
        raise RuntimeError("Dịch vụ email trả dữ liệu không đúng định dạng.")
    out=[]
    for item in data[:10]:
        mid=item.get("id"); subject=item.get("subject") or "(Không có tiêu đề)"
        sender=item.get("from") or "Không rõ"; created=item.get("date") or ""
        text=subject
        if mid is not None:
            try:
                detail=request_json("https://www.1secmail.com/api/v1/?"+urlencode({"action":"readMessage","login":login,"domain":domain,"id":mid}))
                text += " " + str(detail.get("textBody") or "") + " " + str(detail.get("htmlBody") or "")
            except Exception:
                pass
        match=re.search(r"(?<!\d)(\d{4,8})(?!\d)", re.sub(r"<[^>]*>"," ",text))
        out.append({"id":str(mid or ""),"subject":subject,"from":sender,"createdAt":created,"code":match.group(1) if match else ""})
    return out

@app.get("/")
def home():
    return make_response(HTML, 200, {"Content-Type":"text/html; charset=utf-8", "Cache-Control":"no-store"})

@app.post("/api/new")
def api_new():
    try:
        return jsonify(email=new_mail())
    except Exception as e:
        return jsonify(error=str(e)), 502

@app.get("/api/messages")
def api_messages():
    try:
        return jsonify(messages=get_messages(), status="Đã kiểm tra hộp thư")
    except Exception as e:
        return jsonify(error=str(e)), 502

@app.get("/health")
def health():
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
