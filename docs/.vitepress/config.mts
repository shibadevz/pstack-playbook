import { defineConfig } from 'vitepress'
import { thaiTokenize } from './theme/thai-tokenize'

export default defineConfig({
  base: '/pstack-playbook/',
  lang: 'th-TH',
  title: 'PStack Playbook',
  description: 'รวม skill, playbook และ principle ของ PStack ว่ามีอะไรบ้าง ใช้ทำอะไร และเรียกอย่างไร',
  cleanUrls: true,
  themeConfig: {
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        // indexing only: functions in themeConfig are dropped from the client bundle, so theme/index.ts sets the query tokenizer
        miniSearch: { options: { tokenize: thaiTokenize } },
        // index-only: <EntityMeta> keeps its situation names in an attribute, so expand them to text, else searching a situation never finds its entities
        _render: async (src, env, md) => {
          const html = md.render(src, env)
          if (env.frontmatter?.search === false) return ''
          return html.replace(/<EntityMeta[^>]*:sits="([^"]*)"[^>]*>/, (_, a) => {
            try { return '<p>' + JSON.parse(a.replace(/&quot;/g, '"').replace(/&amp;/g, '&')).map(s => s.title).join(' ') + '</p>' } catch { return '' }
          })
        },
        translations: {
          button: { buttonText: 'ค้นหา', buttonAriaLabel: 'ค้นหา' },
          modal: {
            displayDetails: 'แสดงรายละเอียด',
            resetButtonTitle: 'ล้างคำค้นหา',
            backButtonTitle: 'ปิดการค้นหา',
            noResultsText: 'ไม่พบผลลัพธ์สำหรับ',
            footer: {
              selectText: 'เลือก',
              selectKeyAriaLabel: 'enter',
              navigateText: 'เลื่อน',
              navigateUpKeyAriaLabel: 'ลูกศรขึ้น',
              navigateDownKeyAriaLabel: 'ลูกศรลง',
              closeText: 'ปิด',
              closeKeyAriaLabel: 'esc'
            }
          }
        }
      }
    },
    outline: { level: [2, 3], label: 'ในหน้านี้' },
    docFooter: { prev: 'ก่อนหน้า', next: 'ถัดไป' },
    nav: [
      {
        "text": "หน้าแรก",
        "link": "/"
      },
      {
        "text": "Skills",
        "link": "/skills/"
      },
      {
        "text": "Playbooks",
        "link": "/playbooks/"
      },
      {
        "text": "Principles",
        "link": "/principles/"
      },
      {
        "text": "ตามสถานการณ์",
        "link": "/situations/"
      }
    ],
    sidebar: [
      {
        "text": "ตามสถานการณ์",
        "collapsed": false,
        "items": [
          {
            "text": "เริ่มงาน/ตั้งค่า",
            "link": "/situations/start-setup"
          },
          {
            "text": "เข้าใจโค้ด",
            "link": "/situations/understand-code"
          },
          {
            "text": "ออกแบบ/วางแผน",
            "link": "/situations/design-plan"
          },
          {
            "text": "สร้างฟีเจอร์",
            "link": "/situations/build-feature"
          },
          {
            "text": "เจอ bug",
            "link": "/situations/found-bug"
          },
          {
            "text": "Review",
            "link": "/situations/review"
          },
          {
            "text": "Verify/เทส",
            "link": "/situations/verify-test"
          },
          {
            "text": "Refactor/เก็บกวาด",
            "link": "/situations/refactor-cleanup"
          },
          {
            "text": "Performance",
            "link": "/situations/performance"
          },
          {
            "text": "เขียนเอกสาร/สื่อสาร",
            "link": "/situations/docs-communication"
          },
          {
            "text": "PR & Ship",
            "link": "/situations/pr-ship"
          },
          {
            "text": "ปล่อยรันเอง/ข้ามคืน",
            "link": "/situations/autonomous-overnight"
          },
          {
            "text": "ปรับแต่ง PStack",
            "link": "/situations/customize-pstack"
          },
          {
            "text": "ปัญหาที่เจอบ่อย",
            "link": "/situations/troubleshooting"
          }
        ]
      },
      {
        "text": "Workflow skills",
        "collapsed": true,
        "items": [
          {
            "text": "architect",
            "link": "/skills/architect"
          },
          {
            "text": "arena",
            "link": "/skills/arena"
          },
          {
            "text": "automate-me",
            "link": "/skills/automate-me"
          },
          {
            "text": "benchmark-checklist",
            "link": "/skills/benchmark-checklist"
          },
          {
            "text": "blast-radius",
            "link": "/skills/blast-radius"
          },
          {
            "text": "bro",
            "link": "/skills/bro"
          },
          {
            "text": "control-cli",
            "link": "/skills/control-cli"
          },
          {
            "text": "control-ui",
            "link": "/skills/control-ui"
          },
          {
            "text": "correct",
            "link": "/skills/correct"
          },
          {
            "text": "create-verification-skill",
            "link": "/skills/create-verification-skill"
          },
          {
            "text": "deslop",
            "link": "/skills/deslop"
          },
          {
            "text": "figure-it-out",
            "link": "/skills/figure-it-out"
          },
          {
            "text": "how",
            "link": "/skills/how"
          },
          {
            "text": "in-your-own-words",
            "link": "/skills/in-your-own-words"
          },
          {
            "text": "interrogate",
            "link": "/skills/interrogate"
          },
          {
            "text": "ketchup",
            "link": "/skills/ketchup"
          },
          {
            "text": "maintain-verification-skill",
            "link": "/skills/maintain-verification-skill"
          },
          {
            "text": "make-bot-ui",
            "link": "/skills/make-bot-ui"
          },
          {
            "text": "no-comments",
            "link": "/skills/no-comments"
          },
          {
            "text": "poteto-help",
            "link": "/skills/poteto-help"
          },
          {
            "text": "poteto-mode",
            "link": "/skills/poteto-mode"
          },
          {
            "text": "pstack-automate",
            "link": "/skills/pstack-automate"
          },
          {
            "text": "pstack-create-skill",
            "link": "/skills/pstack-create-skill"
          },
          {
            "text": "recall",
            "link": "/skills/recall"
          },
          {
            "text": "reflect",
            "link": "/skills/reflect"
          },
          {
            "text": "setup-pstack",
            "link": "/skills/setup-pstack"
          },
          {
            "text": "sharpen",
            "link": "/skills/sharpen"
          },
          {
            "text": "show-me-your-work",
            "link": "/skills/show-me-your-work"
          },
          {
            "text": "swarm",
            "link": "/skills/swarm"
          },
          {
            "text": "tdd",
            "link": "/skills/tdd"
          },
          {
            "text": "teach",
            "link": "/skills/teach"
          },
          {
            "text": "technical-writing",
            "link": "/skills/technical-writing"
          },
          {
            "text": "typescript-best-practices",
            "link": "/skills/typescript-best-practices"
          },
          {
            "text": "unslop",
            "link": "/skills/unslop"
          },
          {
            "text": "why",
            "link": "/skills/why"
          }
        ]
      },
      {
        "text": "Playbooks",
        "collapsed": true,
        "items": [
          {
            "text": "Investigation",
            "link": "/playbooks/investigation"
          },
          {
            "text": "Bug fix",
            "link": "/playbooks/bug-fix"
          },
          {
            "text": "Perf issue",
            "link": "/playbooks/perf-issue"
          },
          {
            "text": "Hillclimb",
            "link": "/playbooks/hillclimb"
          },
          {
            "text": "Runtime forensics",
            "link": "/playbooks/runtime-forensics"
          },
          {
            "text": "Trace forensics",
            "link": "/playbooks/trace-forensics"
          },
          {
            "text": "Feature",
            "link": "/playbooks/feature"
          },
          {
            "text": "Refactoring",
            "link": "/playbooks/refactoring"
          },
          {
            "text": "Prototype",
            "link": "/playbooks/prototype"
          },
          {
            "text": "Visual parity",
            "link": "/playbooks/visual-parity"
          },
          {
            "text": "Authoring or modifying a skill",
            "link": "/playbooks/authoring-or-modifying-a-skill"
          },
          {
            "text": "Eval",
            "link": "/playbooks/eval"
          },
          {
            "text": "Babysit",
            "link": "/playbooks/babysit"
          },
          {
            "text": "Shipping",
            "link": "/playbooks/shipping"
          },
          {
            "text": "Autonomous run",
            "link": "/playbooks/autonomous-run"
          },
          {
            "text": "Orchestrate",
            "link": "/playbooks/orchestrate"
          },
          {
            "text": "Autopilot-full",
            "link": "/playbooks/autopilot-full"
          },
          {
            "text": "Autopilot-stack",
            "link": "/playbooks/autopilot-stack"
          },
          {
            "text": "Session pickup",
            "link": "/playbooks/session-pickup"
          },
          {
            "text": "Pause safely",
            "link": "/playbooks/pause-safely"
          },
          {
            "text": "Multi-phase or multi-PR plan",
            "link": "/playbooks/multi-phase-or-multi-pr-plan"
          },
          {
            "text": "Worktree and simulator cleanup",
            "link": "/playbooks/worktree-and-simulator-cleanup"
          },
          {
            "text": "Opening a PR",
            "link": "/playbooks/opening-a-pr"
          }
        ]
      },
      {
        "text": "Principles",
        "collapsed": true,
        "items": [
          {
            "text": "attack-the-premise",
            "link": "/principles/attack-the-premise"
          },
          {
            "text": "boundary-discipline",
            "link": "/principles/boundary-discipline"
          },
          {
            "text": "build-the-lever",
            "link": "/principles/build-the-lever"
          },
          {
            "text": "encode-lessons-in-structure",
            "link": "/principles/encode-lessons-in-structure"
          },
          {
            "text": "exhaust-the-design-space",
            "link": "/principles/exhaust-the-design-space"
          },
          {
            "text": "experience-first",
            "link": "/principles/experience-first"
          },
          {
            "text": "explain-the-number",
            "link": "/principles/explain-the-number"
          },
          {
            "text": "fix-root-causes",
            "link": "/principles/fix-root-causes"
          },
          {
            "text": "foundational-thinking",
            "link": "/principles/foundational-thinking"
          },
          {
            "text": "guard-the-context-window",
            "link": "/principles/guard-the-context-window"
          },
          {
            "text": "laziness-protocol",
            "link": "/principles/laziness-protocol"
          },
          {
            "text": "make-operations-idempotent",
            "link": "/principles/make-operations-idempotent"
          },
          {
            "text": "migrate-callers-then-delete-legacy-apis",
            "link": "/principles/migrate-callers-then-delete-legacy-apis"
          },
          {
            "text": "minimize-reader-load",
            "link": "/principles/minimize-reader-load"
          },
          {
            "text": "model-the-domain",
            "link": "/principles/model-the-domain"
          },
          {
            "text": "never-block-on-the-human",
            "link": "/principles/never-block-on-the-human"
          },
          {
            "text": "outcome-oriented-execution",
            "link": "/principles/outcome-oriented-execution"
          },
          {
            "text": "prove-it-works",
            "link": "/principles/prove-it-works"
          },
          {
            "text": "redesign-from-first-principles",
            "link": "/principles/redesign-from-first-principles"
          },
          {
            "text": "separate-before-serializing-shared-state",
            "link": "/principles/separate-before-serializing-shared-state"
          },
          {
            "text": "sequence-verifiable-units",
            "link": "/principles/sequence-verifiable-units"
          },
          {
            "text": "subtract-before-you-add",
            "link": "/principles/subtract-before-you-add"
          },
          {
            "text": "test-behavior-not-implementation",
            "link": "/principles/test-behavior-not-implementation"
          },
          {
            "text": "type-system-discipline",
            "link": "/principles/type-system-discipline"
          }
        ]
      }
    ],
    socialLinks: []
  }
})
