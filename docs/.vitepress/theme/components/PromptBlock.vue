<script setup lang="ts">
import { computed, ref } from 'vue'

const props = defineProps<{ text: string; compact?: boolean }>()
const state = ref<'idle' | 'ok' | 'fail'>('idle')
let timer: ReturnType<typeof setTimeout> | undefined

const cmd = computed(() => props.text.match(/^\/\S+/)?.[0])
const ariaLabel = computed(() => (cmd.value ? `คัดลอก prompt ${cmd.value}` : 'คัดลอก prompt'))
const label = computed(() => ({ idle: 'คัดลอก', ok: 'คัดลอกแล้ว', fail: 'คัดลอกไม่สำเร็จ' })[state.value])

async function copy() {
  try {
    await navigator.clipboard.writeText(props.text)
    state.value = 'ok'
  } catch {
    state.value = 'fail'
  }
  clearTimeout(timer)
  timer = setTimeout(() => (state.value = 'idle'), 1500)
}
</script>

<template>
  <div class="prompt" :class="{ compact }">
    <div class="prompt-bar">
      <span class="prompt-label">ตัวอย่าง prompt</span>
      <button type="button" class="prompt-copy" :data-state="state" :aria-label="ariaLabel" @click="copy">{{ label }}</button>
    </div>
    <pre class="prompt-body"><span class="prompt-caret" aria-hidden="true">❯</span><code>{{ text }}</code></pre>
    <span class="sr-only" role="status">{{ state === 'idle' ? '' : label }}</span>
  </div>
</template>
