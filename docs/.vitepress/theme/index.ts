import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import homeData from './home-data.json'
import PromptBlock from './components/PromptBlock.vue'
import EntityMeta from './components/EntityMeta.vue'
import HomeSheet from './components/HomeSheet.vue'
import { thaiTokenize } from './thai-tokenize'
import './style.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'nav-bar-title-after': () => h('span', { class: 'title-version' }, homeData.upstreamVersion),
    'doc-after': () => h('p', { class: 'upstream-note' }, homeData.upstream)
  }),
  enhanceApp({ app, siteData }) {
    app.component('PromptBlock', PromptBlock)
    app.component('EntityMeta', EntityMeta)
    app.component('HomeSheet', HomeSheet)
    // functions in config never reach the client bundle, so the query tokenizer is attached here
    // dev freezes the nested objects, so clone the path instead of mutating it
    const sd = siteData.value
    const search = sd.themeConfig?.search
    if (search?.provider === 'local') {
      const ms = search.options?.miniSearch
      siteData.value = {
        ...sd,
        themeConfig: {
          ...sd.themeConfig,
          search: {
            ...search,
            options: {
              ...search.options,
              miniSearch: { ...ms, searchOptions: { ...ms?.searchOptions, tokenize: thaiTokenize } }
            }
          }
        }
      }
    }
  }
}
