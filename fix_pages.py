#!/usr/bin/env python3
# Final corrective: expand page0 content

with open('/Users/apple/Documents/面对对象/面对对象教程/basics.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find what page0 body currently looks like
import re
m = re.search(r'<!-- 第1页[^>]*?-->(.*?)<!-- 第2页', content, re.DOTALL)
if m:
    print("Found page0 block:")
    print(repr(m.group(1)[:400]))
else:
    print("Could not find page0 block by comment anchors")

# Replace the old brief page0 card with a richer one
old_card = '<div class="concept-card">\n      <h2 class="concept-title">📝 第一章：复习"类"与"对象"</h2>\n      <p style="font-size: 1.2rem;"><b>类 (Class) 就像一张神奇的"图纸"或"模具"！</b></p>\n      <p style="font-size: 1.2rem;"><b>对象 (Object) 就是根据图纸造出来的"实物"！</b></p>\n    </div>'

new_card = '''<div class="concept-card">
      <h2 class="concept-title">📝 第一章：认识"类"与"对象"</h2>
      <p style="font-size: 1.2rem;"><b>🏗️ 类 (Class)</b>：就像一份神奇的「设计图纸」或「饼干模具」。它描述了将要做出来的东西<b>有哪些特征</b>，以及<b>能做什么动作</b>，但图纸本身不是真实的猫——它只是一个设计方案。</p>
      <p style="font-size: 1.2rem;"><b>🐱 对象 (Object)</b>：就是用图纸真实造出来的「实物」！用猫的图纸，可以造出好多只真实的猫：黑猫汤姆、白猫泡面……它们每一只都是一个「对象」。</p>
      <p style="background:#fff3e0; border-radius:10px; padding: 15px; font-size: 1.1rem; line-height: 1.8; color: #7d6608;">🍪 <b>换个例子更好懂：</b><br>「饼干模具」就是类，决定了饼干的形状；<br>用模具压出来的每一片饼干就是对象。<br>同一个模具能压出很多片饼干（好多对象），每片可以有不同口味（属性值不同）。</p>
    </div>'''

if old_card in content:
    content = content.replace(old_card, new_card, 1)
    print("OK: expanded page0 card")
else:
    print("Old card not found exactly. Trying repr match...")
    idx = content.find('复习"类"与"对象"')
    if idx >= 0:
        print("The title is at index", idx)
        print(repr(content[idx-50:idx+200]))

# Also replace the old "三大法宝" teaser with new text
old_teaser = '<p style="font-size: 1.3rem; text-align: center; color: #e17055; font-weight: bold;">💡 接下来，我们要学习面向对象编程最神奇的<br>"三大法宝（特性）"啦！点击下一页！</p>'
new_teaser = '<p style="font-size: 1.2rem; text-align: center; background: #dfe6e9; border-radius: 10px; padding: 15px; color: #2d3436;">⬇️ 接下来，我们一起学习图纸里最关键的两个知识：<br><b style="color:#6c5ce7; font-size:1.3rem;">「属性」和「方法」</b>，点击下一页！</p>'
if old_teaser in content:
    content = content.replace(old_teaser, new_teaser, 1)
    print("OK: updated page0 teaser text")
else:
    print("Old teaser not found")

with open('/Users/apple/Documents/面对对象/面对对象教程/basics.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
