// news-image-20261123 entry (Node 22, standard library only).
// The image is entry.png beside this file; the program copies it to
// /output/entry.png, the one file the judge reads, and makes it
// world-readable (mode 0644) so the grader can collect it.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// entry.png was drawn in this session by draw.py (Pillow): a newspaper
// front page summing up world news of Monday 23 November 2026.

import { chmodSync, copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
const target = join(outDir, 'entry.png');
copyFileSync(new URL('./entry.png', import.meta.url), target);
chmodSync(target, 0o644);
