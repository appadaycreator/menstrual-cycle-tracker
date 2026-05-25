TITLE = '生理周期トラッカー【無料】次回予測・体調管理'
DESCRIPTION = '生理周期を記録して次回予測日・排卵日を計算。体調の波を把握して毎月の計画を立てやすくするシンプルな周期管理ツール。'
DESCRIPTION_SHORT = '生理周期を記録して次回予測日・排卵日を計算します...'
COLOR1 = '#FFF1F2'
COLOR2 = '#FFE4E6'
COLOR_BTN = '#E11D48'
FOOTER_LINKS = [('https://appadaycreator.com/water-intake-calculator/', '1日の水分摂取量計算ツール'), ('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー'), ('https://appadaycreator.com/vitamin-deficiency-checker/', 'ビタミン不足チェック')]

CUSTOM_CSS = ""

MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:12px;">🌸 生理周期トラッカー</h2>
  <p style="color:#666;font-size:14px;margin-bottom:16px;">最終生理開始日と平均周期を入力して次回予測日を計算します</p>
  <label>最終生理開始日</label>
  <input type="date" id="last-date">
  <label>平均生理周期（日数）</label>
  <div style="display:flex;align-items:center;gap:8px;margin-top:4px;">
    <input type="range" id="cycle-range" min="21" max="40" value="28" style="flex:1;padding:0;border:none;" oninput="document.getElementById('cycle-val').textContent=this.value">
    <span id="cycle-val" style="font-size:20px;font-weight:700;color:#E11D48;min-width:36px;text-align:center;">28</span>
    <span style="font-size:13px;color:#888;">日</span>
  </div>
  <label>生理期間（日数）</label>
  <div style="display:flex;align-items:center;gap:8px;margin-top:4px;">
    <input type="range" id="period-range" min="2" max="10" value="5" style="flex:1;padding:0;border:none;" oninput="document.getElementById('period-val').textContent=this.value">
    <span id="period-val" style="font-size:20px;font-weight:700;color:#E11D48;min-width:24px;text-align:center;">5</span>
    <span style="font-size:13px;color:#888;">日間</span>
  </div>
  <button class="btn" style="margin-top:20px;" onclick="calc()">計算する →</button>
</div>
<div class="result" id="result">
  <div class="card">
    <h3 style="font-size:16px;font-weight:700;color:#E11D48;margin-bottom:12px;">📅 今後3ヶ月の予測</h3>
    <div id="r-list"></div>
    <div style="background:#FFF1F2;border-radius:10px;padding:14px;margin-top:12px;font-size:13px;color:#555;line-height:1.8;">
      <strong>⚠️ 注意事項</strong><br>
      このツールの予測は平均値に基づく参考値です。実際の周期は体調・ストレスで変動します。妊娠・疾患の疑いがある場合は必ず医療機関にご相談ください。
    </div>
    <button class="btn" style="margin-top:16px;" onclick="location.reload()">リセット</button>
  </div>
</div>"""

JS_CODE = """function calc() {{
  const lastStr=document.getElementById('last-date').value;
  if(!lastStr){{alert('最終生理開始日を入力してください');return;}}
  const cycle=parseInt(document.getElementById('cycle-range').value);
  const period=parseInt(document.getElementById('period-range').value);
  const last=new Date(lastStr);
  const rows=[];
  for(let i=1;i<=3;i++){{
    const start=new Date(last); start.setDate(start.getDate()+cycle*i);
    const end=new Date(start); end.setDate(end.getDate()+period-1);
    const ovul=new Date(last); ovul.setDate(ovul.getDate()+cycle*i-14);
    const fertile1=new Date(ovul); fertile1.setDate(fertile1.getDate()-2);
    const fertile2=new Date(ovul); fertile2.setDate(fertile2.getDate()+2);
    const fmt=d=>d.getFullYear()+'/'+(d.getMonth()+1)+'/'+(d.getDate());
    rows.push(`<div style="border-left:4px solid #E11D48;padding:10px 14px;margin-bottom:10px;background:#fff9f9;border-radius:0 8px 8px 0;">
      <div style="font-weight:700;color:#E11D48;">${{i}}ヶ月後</div>
      <div style="font-size:14px;margin-top:4px;">🩸 生理: <strong>${{fmt(start)}} 〜 ${{fmt(end)}}</strong></div>
      <div style="font-size:14px;">🥚 排卵予定: <strong>${{fmt(ovul)}}</strong></div>
      <div style="font-size:13px;color:#888;">妊娠可能期間: ${{fmt(fertile1)}} 〜 ${{fmt(fertile2)}}</div>
    </div>`);
  }}
  document.getElementById('r-list').innerHTML=rows.join('');
  document.getElementById('result').classList.add('show');
  document.getElementById('result').scrollIntoView({{behavior:'smooth'}});
}}"""
