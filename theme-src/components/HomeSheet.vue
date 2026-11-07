<script setup lang="ts">
import { withBase } from 'vitepress'
import data from '../home-data.json'

type Item = { cmd: string; what: string; link: string }
const groups: { key: string; title: string; items: Item[] }[] = data.groups
</script>

<template>
  <main class="sheet">
    <header class="sheet-top">
      <h1>PStack Playbook</h1>
      <p>รวมคำสั่ง /pstack: ที่พิมพ์ใน Claude Code ว่าตัวไหนใช้ทำอะไรและควรใช้เมื่อไหร่ กดชื่อเพื่อดูตัวอย่าง prompt ที่คัดลอกไปวางได้เลย</p>
      <p class="upstream-note">{{ data.upstream }}</p>
      <div class="mock" aria-hidden="true"><span class="mock-caret">❯</span><span>/pstack:</span><span class="blink"></span></div>
    </header>

    <section class="sheet-sec" aria-labelledby="sec-situations">
      <h2 id="sec-situations">ตามสถานการณ์<span class="count">{{ data.situations.length }}</span></h2>
      <ul class="sheet-sits">
        <li v-for="s in data.situations" :key="s.link"><a :href="withBase(s.link)">{{ s.title }}</a></li>
      </ul>
    </section>

    <section v-for="g in groups" :key="g.key" class="sheet-sec" :aria-labelledby="'sec-' + g.key">
      <h2 :id="'sec-' + g.key"><i :data-type="g.key" aria-hidden="true"></i>{{ g.title }}<span class="count">{{ g.items.length }}</span></h2>
      <ul class="sheet-grid">
        <li v-for="it in g.items" :key="it.link">
          <a class="cmd" :href="withBase(it.link)">{{ it.cmd }}</a>
          <p>{{ it.what }}</p>
        </li>
      </ul>
    </section>
  </main>
</template>
