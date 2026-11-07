// MiniSearch splits on whitespace only, so a Thai sentence would be one token. Shared by the build-time index and the client query.
let seg: Intl.Segmenter | undefined

export function thaiTokenize(text: string): string[] {
  if (typeof Intl === 'undefined' || !Intl.Segmenter) return text.split(/[\s\p{P}]+/u).filter(Boolean)
  seg ??= new Intl.Segmenter('th', { granularity: 'word' })
  const out: string[] = []
  for (const s of seg.segment(text)) if (s.isWordLike) out.push(s.segment)
  return out
}
