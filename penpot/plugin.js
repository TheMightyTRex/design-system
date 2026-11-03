// Made by penpot/make.py from plugin.src.js, tokens.css and icons.svg: change those, not this file.
// @ts-check
// TRex Design System for Penpot: builds the design system into the open file. penpot/make.py writes the
// library's values in place of DATA and saves the result as plugin.js; change this file, then run make.py.

/** @type {{font: string, themes: Record<string, Record<string, {hex: string, opacity: number}>>,
 *  core: {space: Record<string, number>, text: Record<string, number>, weight: Record<string, number>, size: Record<string, number>},
 *  icons: Record<string, string>}} */
// @ts-ignore: written by make.py
const DATA = {"font":"Atkinson Hyperlegible Next","themes":{"Light":{"color-bg":{"hex":"#f0f5ff","opacity":1},"color-header":{"hex":"#fcfdff","opacity":1},"color-surface":{"hex":"#f7faff","opacity":1},"color-surface-raised":{"hex":"#ffffff","opacity":1},"color-surface-sunken":{"hex":"#e4ebf7","opacity":1},"color-text":{"hex":"#141416","opacity":1},"color-text-muted":{"hex":"#424b5b","opacity":1},"color-border":{"hex":"#7d879a","opacity":1},"color-divider":{"hex":"#c2cddf","opacity":1},"color-accent":{"hex":"#0b5f5a","opacity":1},"color-accent-text":{"hex":"#ffffff","opacity":1},"color-accent-soft":{"hex":"#dff1ef","opacity":1},"color-panel-header":{"hex":"#ffffff","opacity":1},"color-scrollbar":{"hex":"#7d879a","opacity":1},"color-scrollbar-hover":{"hex":"#424b5b","opacity":1},"color-slide-header":{"hex":"#f0f5ff","opacity":1},"color-control-active":{"hex":"#0b5f5a","opacity":0.12},"color-focus":{"hex":"#0b5f5a","opacity":1},"color-count":{"hex":"#af4e24","opacity":1},"color-count-text":{"hex":"#ffffff","opacity":1},"color-backdrop":{"hex":"#101828","opacity":0.45},"color-logo-tile":{"hex":"#323a77","opacity":1},"color-logo-star":{"hex":"#af4e24","opacity":1},"chart-1":{"hex":"#4552a8","opacity":1},"chart-2":{"hex":"#c0602f","opacity":1},"series-1":{"hex":"#2a78d6","opacity":1},"series-2":{"hex":"#eb6834","opacity":1},"series-3":{"hex":"#1baf7a","opacity":1},"series-4":{"hex":"#eda100","opacity":1},"series-5":{"hex":"#e87ba4","opacity":1},"series-6":{"hex":"#008300","opacity":1},"series-7":{"hex":"#6250d6","opacity":1},"series-empty":{"hex":"#dfe5ef","opacity":1},"series-empty-line":{"hex":"#b9c2d1","opacity":1},"status-success-bg":{"hex":"#dcf2e3","opacity":1},"status-success-fg":{"hex":"#135c2e","opacity":1},"status-info-bg":{"hex":"#dde9fb","opacity":1},"status-info-fg":{"hex":"#154a96","opacity":1},"status-neutral-bg":{"hex":"#eceef2","opacity":1},"status-neutral-fg":{"hex":"#3c4350","opacity":1},"status-warning-bg":{"hex":"#fdefc8","opacity":1},"status-warning-fg":{"hex":"#6b4500","opacity":1},"status-danger-bg":{"hex":"#fbe0de","opacity":1},"status-danger-fg":{"hex":"#9b1c14","opacity":1},"status-muted-bg":{"hex":"#eceef2","opacity":1},"status-muted-fg":{"hex":"#4a5160","opacity":1}},"Dark":{"color-bg":{"hex":"#101827","opacity":1},"color-header":{"hex":"#141e2e","opacity":1},"color-surface":{"hex":"#1c2738","opacity":1},"color-surface-raised":{"hex":"#232f42","opacity":1},"color-surface-sunken":{"hex":"#0c1220","opacity":1},"color-text":{"hex":"#f3f4f6","opacity":1},"color-text-muted":{"hex":"#a4aec1","opacity":1},"color-border":{"hex":"#6f7b91","opacity":1},"color-divider":{"hex":"#303c51","opacity":1},"color-accent":{"hex":"#5ed3c6","opacity":1},"color-accent-text":{"hex":"#101827","opacity":1},"color-accent-soft":{"hex":"#163a38","opacity":1},"color-panel-header":{"hex":"#232f42","opacity":1},"color-scrollbar":{"hex":"#6f7b91","opacity":1},"color-scrollbar-hover":{"hex":"#a4aec1","opacity":1},"color-slide-header":{"hex":"#101827","opacity":1},"color-control-active":{"hex":"#5ed3c6","opacity":0.12},"color-focus":{"hex":"#5ed3c6","opacity":1},"color-count":{"hex":"#b7562c","opacity":1},"color-count-text":{"hex":"#ffffff","opacity":1},"color-backdrop":{"hex":"#000000","opacity":0.6},"color-logo-tile":{"hex":"#a5b4fc","opacity":1},"color-logo-star":{"hex":"#ffb38a","opacity":1},"chart-1":{"hex":"#6f80e6","opacity":1},"chart-2":{"hex":"#d2733c","opacity":1},"series-1":{"hex":"#3987e5","opacity":1},"series-2":{"hex":"#d95926","opacity":1},"series-3":{"hex":"#199e70","opacity":1},"series-4":{"hex":"#c98500","opacity":1},"series-5":{"hex":"#d55181","opacity":1},"series-6":{"hex":"#2fa82f","opacity":1},"series-7":{"hex":"#9085e9","opacity":1},"series-empty":{"hex":"#3a475c","opacity":1},"series-empty-line":{"hex":"#56647b","opacity":1},"status-success-bg":{"hex":"#12351f","opacity":1},"status-success-fg":{"hex":"#8fe0aa","opacity":1},"status-info-bg":{"hex":"#142a4b","opacity":1},"status-info-fg":{"hex":"#a8c8ff","opacity":1},"status-neutral-bg":{"hex":"#262a33","opacity":1},"status-neutral-fg":{"hex":"#c9ced8","opacity":1},"status-warning-bg":{"hex":"#3a2c09","opacity":1},"status-warning-fg":{"hex":"#f6cf6b","opacity":1},"status-danger-bg":{"hex":"#431816","opacity":1},"status-danger-fg":{"hex":"#ffaaa3","opacity":1},"status-muted-bg":{"hex":"#262a33","opacity":1},"status-muted-fg":{"hex":"#b3b9c5","opacity":1}},"High contrast":{"color-bg":{"hex":"#f0f5ff","opacity":1},"color-header":{"hex":"#ffffff","opacity":1},"color-surface":{"hex":"#ffffff","opacity":1},"color-surface-raised":{"hex":"#ffffff","opacity":1},"color-surface-sunken":{"hex":"#f0f0f0","opacity":1},"color-text":{"hex":"#030304","opacity":1},"color-text-muted":{"hex":"#19212f","opacity":1},"color-border":{"hex":"#000000","opacity":1},"color-divider":{"hex":"#596272","opacity":1},"color-accent":{"hex":"#003d39","opacity":1},"color-accent-text":{"hex":"#ffffff","opacity":1},"color-accent-soft":{"hex":"#d6eeeb","opacity":1},"color-panel-header":{"hex":"#ffffff","opacity":1},"color-scrollbar":{"hex":"#030304","opacity":1},"color-scrollbar-hover":{"hex":"#030304","opacity":1},"color-slide-header":{"hex":"#f0f5ff","opacity":1},"color-control-active":{"hex":"#003d39","opacity":0.12},"color-focus":{"hex":"#c4006a","opacity":1},"color-count":{"hex":"#863309","opacity":1},"color-count-text":{"hex":"#ffffff","opacity":1},"color-backdrop":{"hex":"#101828","opacity":0.45},"color-logo-tile":{"hex":"#11104a","opacity":1},"color-logo-star":{"hex":"#863309","opacity":1},"chart-1":{"hex":"#1f2a8a","opacity":1},"chart-2":{"hex":"#8a3200","opacity":1},"series-1":{"hex":"#1f5fbf","opacity":1},"series-2":{"hex":"#c4471b","opacity":1},"series-3":{"hex":"#00806a","opacity":1},"series-4":{"hex":"#946000","opacity":1},"series-5":{"hex":"#b8336a","opacity":1},"series-6":{"hex":"#006b00","opacity":1},"series-7":{"hex":"#5440c8","opacity":1},"series-empty":{"hex":"#ffffff","opacity":1},"series-empty-line":{"hex":"#767676","opacity":1},"status-success-bg":{"hex":"#dcf2e3","opacity":1},"status-success-fg":{"hex":"#003d17","opacity":1},"status-info-bg":{"hex":"#dde9fb","opacity":1},"status-info-fg":{"hex":"#00266e","opacity":1},"status-neutral-bg":{"hex":"#eceef2","opacity":1},"status-neutral-fg":{"hex":"#000000","opacity":1},"status-warning-bg":{"hex":"#fdefc8","opacity":1},"status-warning-fg":{"hex":"#3d2600","opacity":1},"status-danger-bg":{"hex":"#fbe0de","opacity":1},"status-danger-fg":{"hex":"#6e0000","opacity":1},"status-muted-bg":{"hex":"#eceef2","opacity":1},"status-muted-fg":{"hex":"#000000","opacity":1}},"High contrast dark":{"color-bg":{"hex":"#000000","opacity":1},"color-header":{"hex":"#000000","opacity":1},"color-surface":{"hex":"#000000","opacity":1},"color-surface-raised":{"hex":"#000000","opacity":1},"color-surface-sunken":{"hex":"#111111","opacity":1},"color-text":{"hex":"#ffffff","opacity":1},"color-text-muted":{"hex":"#d5e0f4","opacity":1},"color-border":{"hex":"#ffffff","opacity":1},"color-divider":{"hex":"#8391aa","opacity":1},"color-accent":{"hex":"#b8f2ea","opacity":1},"color-accent-text":{"hex":"#000000","opacity":1},"color-accent-soft":{"hex":"#0b2a27","opacity":1},"color-panel-header":{"hex":"#000000","opacity":1},"color-scrollbar":{"hex":"#ffffff","opacity":1},"color-scrollbar-hover":{"hex":"#ffffff","opacity":1},"color-slide-header":{"hex":"#000000","opacity":1},"color-control-active":{"hex":"#b8f2ea","opacity":0.12},"color-focus":{"hex":"#ffd400","opacity":1},"color-count":{"hex":"#a44418","opacity":1},"color-count-text":{"hex":"#ffffff","opacity":1},"color-backdrop":{"hex":"#000000","opacity":0.6},"color-logo-tile":{"hex":"#e7ecff","opacity":1},"color-logo-star":{"hex":"#ffc7a6","opacity":1},"chart-1":{"hex":"#c2cbff","opacity":1},"chart-2":{"hex":"#ffb38a","opacity":1},"series-1":{"hex":"#3987e5","opacity":1},"series-2":{"hex":"#d95926","opacity":1},"series-3":{"hex":"#199e70","opacity":1},"series-4":{"hex":"#c98500","opacity":1},"series-5":{"hex":"#d55181","opacity":1},"series-6":{"hex":"#2fa82f","opacity":1},"series-7":{"hex":"#9085e9","opacity":1},"series-empty":{"hex":"#000000","opacity":1},"series-empty-line":{"hex":"#8a8a8a","opacity":1},"status-success-bg":{"hex":"#002b10","opacity":1},"status-success-fg":{"hex":"#a6ffc2","opacity":1},"status-info-bg":{"hex":"#001c45","opacity":1},"status-info-fg":{"hex":"#c2dbff","opacity":1},"status-neutral-bg":{"hex":"#1a1a1a","opacity":1},"status-neutral-fg":{"hex":"#ffffff","opacity":1},"status-warning-bg":{"hex":"#2e2000","opacity":1},"status-warning-fg":{"hex":"#ffe08a","opacity":1},"status-danger-bg":{"hex":"#330000","opacity":1},"status-danger-fg":{"hex":"#ffc2bd","opacity":1},"status-muted-bg":{"hex":"#1a1a1a","opacity":1},"status-muted-fg":{"hex":"#ffffff","opacity":1}}},"core":{"space":{"space-1":4,"space-2":8,"space-3":12,"space-4":16,"space-5":20,"space-6":24,"space-8":32,"space-10":40,"space-12":48},"text":{"text-xs":12,"text-sm":14,"text-md":16,"text-lg":20,"text-xl":24,"text-2xl":32},"weight":{"weight-regular":400,"weight-strong":600,"weight-heading":700},"size":{"control-h":44,"control-h-compact":32,"icon-sm":16,"icon-md":18,"icon-lg":20,"header-h":64,"tabs-h":48,"rail-w":88,"panel-w":420,"dialog-w":560,"focus-w":3,"status-edge-w":6}},"icons":{"book-open":"<path d=\"M12 5v16\"/><path d=\"M20.001 19A2 2 0 0022 17V5a2 2 0 00-1.999-2L16 3.002A5 5 0 0012 5a5 5 0 00-4-2H4a2 2 0 00-2 2v12a2 2 0 001.999 2H8a5 5 0 014 2 5 5 0 014-2z\"/>","bookmark":"<path d=\"M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z\"/>","list-checks":"<path d=\"M13 5h8\"/><path d=\"M13 12h8\"/><path d=\"M13 19h8\"/><path d=\"m3 17 2 2 4-4\"/><path d=\"m3 7 2 2 4-4\"/>","compass":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"m16.24 7.76-1.804 5.411a2 2 0 0 1-1.265 1.265L7.76 16.24l1.804-5.411a2 2 0 0 1 1.265-1.265z\"/>","activity":"<path d=\"M22 12h-2.48a2 2 0 0 0-1.93 1.46l-2.35 8.36a.25.25 0 0 1-.48 0L9.24 2.18a.25.25 0 0 0-.48 0l-2.35 8.36A2 2 0 0 1 4.49 12H2\"/>","settings":"<path d=\"M9.671 4.136a2.34 2.34 0 0 1 4.659 0 2.34 2.34 0 0 0 3.319 1.915 2.34 2.34 0 0 1 2.33 4.033 2.34 2.34 0 0 0 0 3.831 2.34 2.34 0 0 1-2.33 4.033 2.34 2.34 0 0 0-3.319 1.915 2.34 2.34 0 0 1-4.659 0 2.34 2.34 0 0 0-3.32-1.915 2.34 2.34 0 0 1-2.33-4.033 2.34 2.34 0 0 0 0-3.831A2.34 2.34 0 0 1 6.35 6.051a2.34 2.34 0 0 0 3.319-1.915\"/><circle cx=\"12\" cy=\"12\" r=\"3\"/>","sparkles":"<path d=\"M11.017 2.814a1 1 0 0 1 1.966 0l1.051 5.558a2 2 0 0 0 1.594 1.594l5.558 1.051a1 1 0 0 1 0 1.966l-5.558 1.051a2 2 0 0 0-1.594 1.594l-1.051 5.558a1 1 0 0 1-1.966 0l-1.051-5.558a2 2 0 0 0-1.594-1.594l-5.558-1.051a1 1 0 0 1 0-1.966l5.558-1.051a2 2 0 0 0 1.594-1.594z\"/><path d=\"M20 2v4\"/><path d=\"M22 4h-4\"/><circle cx=\"4\" cy=\"20\" r=\"2\"/>","library":"<path d=\"m16 6 4 14\"/><path d=\"M12 6v14\"/><path d=\"M8 8v12\"/><path d=\"M4 4v16\"/>","layout-grid":"<rect width=\"7\" height=\"7\" x=\"3\" y=\"3\" rx=\"1\"/><rect width=\"7\" height=\"7\" x=\"14\" y=\"3\" rx=\"1\"/><rect width=\"7\" height=\"7\" x=\"14\" y=\"14\" rx=\"1\"/><rect width=\"7\" height=\"7\" x=\"3\" y=\"14\" rx=\"1\"/>","calendar-days":"<path d=\"M8 2v3\"/><path d=\"M16 2v3\"/><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><path d=\"M3 9h18\"/><path d=\"M8 13h.01\"/><path d=\"M12 13h.01\"/><path d=\"M16 13h.01\"/><path d=\"M8 17h.01\"/><path d=\"M12 17h.01\"/><path d=\"M16 17h.01\"/>","layers":"<path d=\"M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z\"/><path d=\"M2 12a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 12\"/><path d=\"M2 17a1 1 0 0 0 .58.91l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9A1 1 0 0 0 22 17\"/>","award":"<path d=\"m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526\"/><circle cx=\"12\" cy=\"8\" r=\"6\"/>","list":"<path d=\"M3 5h.01\"/><path d=\"M3 12h.01\"/><path d=\"M3 19h.01\"/><path d=\"M8 5h13\"/><path d=\"M8 12h13\"/><path d=\"M8 19h13\"/>","menu":"<path d=\"M4 5h16\"/><path d=\"M4 12h16\"/><path d=\"M4 19h16\"/>","x":"<path d=\"M18 6 6 18\"/><path d=\"m6 6 12 12\"/>","search":"<path d=\"m21 21-4.34-4.34\"/><circle cx=\"11\" cy=\"11\" r=\"8\"/>","sun":"<circle cx=\"12\" cy=\"12\" r=\"4\"/><path d=\"M12 2v2\"/><path d=\"M12 20v2\"/><path d=\"m4.93 4.93 1.41 1.41\"/><path d=\"m17.66 17.66 1.41 1.41\"/><path d=\"M2 12h2\"/><path d=\"M20 12h2\"/><path d=\"m6.34 17.66-1.41 1.41\"/><path d=\"m19.07 4.93-1.41 1.41\"/>","chevron-down":"<path d=\"m6 9 6 6 6-6\"/>","chevron-right":"<path d=\"m9 18 6-6-6-6\"/>","check":"<path d=\"M20 6 9 17l-5-5\"/>","plus":"<path d=\"M5 12h14\"/><path d=\"M12 5v14\"/>","refresh-cw":"<path d=\"M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8\"/><path d=\"M21 3v5h-5\"/><path d=\"M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16\"/><path d=\"M8 16H3v5\"/>","download":"<path d=\"M12 15V3\"/><path d=\"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\"/><path d=\"m7 10 5 5 5-5\"/>","copy":"<rect width=\"14\" height=\"14\" x=\"8\" y=\"8\" rx=\"2\" ry=\"2\"/><path d=\"M4 16c-1.1 0-2-.9-2-2V4c0-1.1.9-2 2-2h10c1.1 0 2 .9 2 2\"/>","circle-help":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3\"/><path d=\"M12 17h.01\"/>","circle-alert":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><line x1=\"12\" x2=\"12\" y1=\"8\" y2=\"12\"/><line x1=\"12\" x2=\"12.01\" y1=\"16\" y2=\"16\"/>","circle-check":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"m16 9-5.5 5.5L8 12\"/>","triangle-alert":"<path d=\"m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3\"/><path d=\"M12 9v4\"/><path d=\"M12 17h.01\"/>","info":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 16v-4\"/><path d=\"M12 8h.01\"/>","trash-2":"<path d=\"M10 11v6\"/><path d=\"M14 11v6\"/><path d=\"M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6\"/><path d=\"M3 6h18\"/><path d=\"M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2\"/>","pencil":"<path d=\"M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z\"/><path d=\"m15 5 4 4\"/>","external-link":"<path d=\"M15 3h6v6\"/><path d=\"M10 14 21 3\"/><path d=\"M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6\"/>","log-out":"<path d=\"m16 17 5-5-5-5\"/><path d=\"M21 12H9\"/><path d=\"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4\"/>","user":"<path d=\"M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2\"/><circle cx=\"12\" cy=\"7\" r=\"4\"/>","users":"<path d=\"M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2\"/><path d=\"M16 3.128a4 4 0 0 1 0 7.744\"/><path d=\"M22 21v-2a4 4 0 0 0-3-3.87\"/><circle cx=\"9\" cy=\"7\" r=\"4\"/>","key-round":"<path d=\"M2.586 17.414A2 2 0 0 0 2 18.828V21a1 1 0 0 0 1 1h3a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h1a1 1 0 0 0 1-1v-1a1 1 0 0 1 1-1h.172a2 2 0 0 0 1.414-.586l.814-.814a6.5 6.5 0 1 0-4-4z\"/><circle cx=\"16.5\" cy=\"7.5\" r=\".5\" fill=\"currentColor\"/>","bell":"<path d=\"M10.268 21a2 2 0 0 0 3.464 0\"/><path d=\"M3.262 15.326A1 1 0 0 0 4 17h16a1 1 0 0 0 .74-1.673C19.41 13.956 18 12.499 18 8A6 6 0 0 0 6 8c0 4.499-1.411 5.956-2.738 7.326\"/>","hard-drive-download":"<path d=\"M12 2v8\"/><path d=\"m16 6-4 4-4-4\"/><rect width=\"20\" height=\"8\" x=\"2\" y=\"14\" rx=\"2\"/><path d=\"M6 18h.01\"/><path d=\"M10 18h.01\"/>","radar":"<path d=\"M19.07 4.93A10 10 0 0 0 6.99 3.34\"/><path d=\"M4 6h.01\"/><path d=\"M2.29 9.62A10 10 0 1 0 21.31 8.35\"/><path d=\"M16.24 7.76A6 6 0 1 0 8.23 16.67\"/><path d=\"M12 18h.01\"/><path d=\"M17.99 11.66A6 6 0 0 1 15.77 16.67\"/><circle cx=\"12\" cy=\"12\" r=\"2\"/><path d=\"m13.41 10.59 5.66-5.66\"/>","sliders-horizontal":"<path d=\"M10 5H3\"/><path d=\"M12 19H3\"/><path d=\"M14 3v4\"/><path d=\"M16 17v4\"/><path d=\"M21 12h-9\"/><path d=\"M21 19h-5\"/><path d=\"M21 5h-7\"/><path d=\"M8 10v4\"/><path d=\"M8 12H3\"/>","zap":"<path d=\"M15.914 4a1.5 1.5 0 00-2.474-1.561l-9 9A1.5 1.5 0 005.5 14h4.002a.5.5 0 01.471.666L8.086 20a1.5 1.5 0 002.475 1.56l9-9A1.5 1.5 0 0018.5 10h-3.997a.5.5 0 01-.472-.667z\"/>","scroll-text":"<path d=\"M15 12h-5\"/><path d=\"M15 8h-5\"/><path d=\"M19 17V5a2 2 0 0 0-2-2H4\"/><path d=\"M8 21h12a2 2 0 0 0 2-2v-1a1 1 0 0 0-1-1H11a1 1 0 0 0-1 1v1a2 2 0 1 1-4 0V5a2 2 0 1 0-4 0v2a1 1 0 0 0 1 1h3\"/>","timer":"<line x1=\"10\" x2=\"14\" y1=\"2\" y2=\"2\"/><line x1=\"12\" x2=\"15\" y1=\"14\" y2=\"11\"/><circle cx=\"12\" cy=\"14\" r=\"8\"/>","archive-restore":"<rect width=\"20\" height=\"5\" x=\"2\" y=\"3\" rx=\"1\"/><path d=\"M4 8v11a2 2 0 0 0 2 2h2\"/><path d=\"M20 8v11a2 2 0 0 1-2 2h-2\"/><path d=\"m9 15 3-3 3 3\"/><path d=\"M12 12v9\"/>","archive":"<rect width=\"20\" height=\"5\" x=\"2\" y=\"3\" rx=\"1\"/><path d=\"M4 8v11a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8\"/><path d=\"M10 12h4\"/>","book-copy":"<path d=\"M5 7a2 2 0 0 0-2 2v11\"/><path d=\"M5.803 18H5a2 2 0 0 0 0 4h9.5a.5.5 0 0 0 .5-.5V21\"/><path d=\"M9 15V4a2 2 0 0 1 2-2h9.5a.5.5 0 0 1 .5.5v14a.5.5 0 0 1-.5.5H11a2 2 0 0 1 0-4h10\"/>","server":"<rect width=\"20\" height=\"8\" x=\"2\" y=\"2\" rx=\"2\" ry=\"2\"/><rect width=\"20\" height=\"8\" x=\"2\" y=\"14\" rx=\"2\" ry=\"2\"/><line x1=\"6\" x2=\"6.01\" y1=\"6\" y2=\"6\"/><line x1=\"6\" x2=\"6.01\" y1=\"18\" y2=\"18\"/>","hard-drive":"<path d=\"M10 16h.01\"/><path d=\"M2.212 11.577a2 2 0 0 0-.212.896V18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-5.527a2 2 0 0 0-.212-.896L18.55 5.11A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z\"/><path d=\"M21.946 12.013H2.054\"/><path d=\"M6 16h.01\"/>","cpu":"<path d=\"M12 20v2\"/><path d=\"M12 2v2\"/><path d=\"M17 20v2\"/><path d=\"M17 2v2\"/><path d=\"M2 12h2\"/><path d=\"M2 17h2\"/><path d=\"M2 7h2\"/><path d=\"M20 12h2\"/><path d=\"M20 17h2\"/><path d=\"M20 7h2\"/><path d=\"M7 20v2\"/><path d=\"M7 2v2\"/><rect x=\"4\" y=\"4\" width=\"16\" height=\"16\" rx=\"2\"/><rect x=\"8\" y=\"8\" width=\"8\" height=\"8\" rx=\"1\"/>","network":"<rect x=\"16\" y=\"16\" width=\"6\" height=\"6\" rx=\"1\"/><rect x=\"2\" y=\"16\" width=\"6\" height=\"6\" rx=\"1\"/><rect x=\"9\" y=\"2\" width=\"6\" height=\"6\" rx=\"1\"/><path d=\"M5 16v-3a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3\"/><path d=\"M12 12V8\"/>","database":"<ellipse cx=\"12\" cy=\"5\" rx=\"9\" ry=\"3\"/><path d=\"M3 5V19A9 3 0 0 0 21 19V5\"/><path d=\"M3 12A9 3 0 0 0 21 12\"/>","play":"<path d=\"M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z\"/>","pause":"<rect x=\"14\" y=\"3\" width=\"5\" height=\"18\" rx=\"1\"/><rect x=\"5\" y=\"3\" width=\"5\" height=\"18\" rx=\"1\"/>","rotate-ccw":"<path d=\"M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8\"/><path d=\"M3 3v5h5\"/>","filter":"<path d=\"M10 20a1 1 0 0 0 .553.895l2 1A1 1 0 0 0 14 21v-7a2 2 0 0 1 .517-1.341L21.74 4.67A1 1 0 0 0 21 3H3a1 1 0 0 0-.742 1.67l7.225 7.989A2 2 0 0 1 10 14z\"/>","arrow-up-down":"<path d=\"m21 16-4 4-4-4\"/><path d=\"M17 20V4\"/><path d=\"m3 8 4-4 4 4\"/><path d=\"M7 4v16\"/>","ellipsis":"<circle cx=\"12\" cy=\"12\" r=\"1\"/><circle cx=\"19\" cy=\"12\" r=\"1\"/><circle cx=\"5\" cy=\"12\" r=\"1\"/>","star":"<path d=\"M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z\"/>","clock":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 6v6l4 2\"/>","history":"<path d=\"M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8\"/><path d=\"M3 3v5h5\"/><path d=\"M12 7v5l4 2\"/>","list-ordered":"<path d=\"M11 5h10\"/><path d=\"M11 12h10\"/><path d=\"M11 19h10\"/><path d=\"M4 4h1v5\"/><path d=\"M4 9h2\"/><path d=\"M6.5 20H3.4c0-1 2.6-1.925 2.6-3.5a1.5 1.5 0 0 0-2.6-1.02\"/>","file-search":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><circle cx=\"11.5\" cy=\"14.5\" r=\"2.5\"/><path d=\"M13.3 16.3 15 18\"/>","heart-pulse":"<path d=\"M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5\"/><path d=\"M3.22 13H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27\"/>","gauge":"<path d=\"m12 14 4-4\"/><path d=\"M3.34 19a10 10 0 1 1 17.32 0\"/>","shield-check":"<path d=\"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z\"/><path d=\"m9 12 2 2 4-4\"/>","folder":"<path d=\"M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z\"/>","link":"<path d=\"M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71\"/><path d=\"M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71\"/>","inbox":"<polyline points=\"22 12 16 12 14 15 10 15 8 12 2 12\"/><path d=\"M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z\"/>","wifi":"<path d=\"M12 20h.01\"/><path d=\"M2 8.82a15 15 0 0 1 20 0\"/><path d=\"M5 12.859a10 10 0 0 1 14 0\"/><path d=\"M8.5 16.429a5 5 0 0 1 7 0\"/>","circle-arrow-up":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"m16 12-4-4-4 4\"/><path d=\"M12 16V8\"/>","server-cog":"<path d=\"m10.852 14.772-.383.923\"/><path d=\"M13.148 14.772a3 3 0 1 0-2.296-5.544l-.383-.923\"/><path d=\"m13.148 9.228.383-.923\"/><path d=\"m13.53 15.696-.382-.924a3 3 0 1 1-2.296-5.544\"/><path d=\"m14.772 10.852.923-.383\"/><path d=\"m14.772 13.148.923.383\"/><path d=\"M4.5 10H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-.5\"/><path d=\"M4.5 14H4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-4a2 2 0 0 0-2-2h-.5\"/><path d=\"M6 18h.01\"/><path d=\"M6 6h.01\"/><path d=\"m9.228 10.852-.923-.383\"/><path d=\"m9.228 13.148-.923.383\"/>","chart-line":"<path d=\"M3 3v16a2 2 0 0 0 2 2h16\"/><path d=\"m19 9-5 5-4-4-3 3\"/>","app-window":"<rect x=\"2\" y=\"4\" width=\"20\" height=\"16\" rx=\"2\"/><path d=\"M10 4v4\"/><path d=\"M2 8h20\"/><path d=\"M6 4v4\"/>","thermometer":"<path d=\"M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z\"/>","globe":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20\"/><path d=\"M2 12h20\"/>","lock":"<rect width=\"18\" height=\"11\" x=\"3\" y=\"11\" rx=\"2\" ry=\"2\"/><path d=\"M7 11V7a5 5 0 0 1 10 0v4\"/>","upload":"<path d=\"M12 3v12\"/><path d=\"m17 8-5-5-5 5\"/><path d=\"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4\"/>","file-text":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><path d=\"M10 9H8\"/><path d=\"M16 13H8\"/><path d=\"M16 17H8\"/>","eye":"<path d=\"M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0\"/><circle cx=\"12\" cy=\"12\" r=\"3\"/>","grip-vertical":"<circle cx=\"9\" cy=\"12\" r=\"1\"/><circle cx=\"9\" cy=\"5\" r=\"1\"/><circle cx=\"9\" cy=\"19\" r=\"1\"/><circle cx=\"15\" cy=\"12\" r=\"1\"/><circle cx=\"15\" cy=\"5\" r=\"1\"/><circle cx=\"15\" cy=\"19\" r=\"1\"/>","arrow-up":"<path d=\"m5 12 7-7 7 7\"/><path d=\"M12 19V5\"/>","arrow-down":"<path d=\"M12 5v14\"/><path d=\"m19 12-7 7-7-7\"/>","panel-right-open":"<rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\"/><path d=\"M15 3v18\"/><path d=\"m10 15-3-3 3-3\"/>","circle-x":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"m15 9-6 6\"/><path d=\"m9 9 6 6\"/>","house":"<path d=\"M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8\"/><path d=\"M3 10a2 2 0 0 1 .709-1.528l7-6a2 2 0 0 1 2.582 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z\"/>","film":"<rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\"/><path d=\"M7 3v18\"/><path d=\"M3 7.5h4\"/><path d=\"M3 12h18\"/><path d=\"M3 16.5h4\"/><path d=\"M17 3v18\"/><path d=\"M17 7.5h4\"/><path d=\"M17 16.5h4\"/>","tv":"<path d=\"m17 2-5 5-5-5\"/><rect width=\"20\" height=\"15\" x=\"2\" y=\"7\" rx=\"2\"/>","music":"<path d=\"M9 18V5l12-2v13\"/><circle cx=\"6\" cy=\"18\" r=\"3\"/><circle cx=\"18\" cy=\"16\" r=\"3\"/>","book":"<path d=\"M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20\"/>","terminal":"<path d=\"M12 19h8\"/><path d=\"m4 17 6-6-6-6\"/>","monitor":"<rect width=\"20\" height=\"14\" x=\"2\" y=\"3\" rx=\"2\"/><line x1=\"8\" x2=\"16\" y1=\"21\" y2=\"21\"/><line x1=\"12\" x2=\"12\" y1=\"17\" y2=\"21\"/>","wrench":"<path d=\"M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.106-3.105c.32-.322.863-.22.983.218a6 6 0 0 1-8.259 7.057l-7.91 7.91a1 1 0 0 1-2.999-3l7.91-7.91a6 6 0 0 1 7.057-8.259c.438.12.54.662.219.984z\"/>","arrow-left":"<path d=\"m12 19-7-7 7-7\"/><path d=\"M19 12H5\"/>","ban":"<circle cx=\"12\" cy=\"12\" r=\"10\"/><path d=\"M4.929 4.929 19.07 19.071\"/>","book-marked":"<path d=\"M10 2v7.751a.25.25 0 00.407.195l2.28-1.834a.5.5 0 01.627 0l2.28 1.834A.25.25 0 0016 9.751V2\"/><path d=\"M4 19.5v-15A2.5 2.5 0 016.5 2H19a1 1 0 011 1v18a1 1 0 01-1 1H6.5a1 1 0 010-5H20\"/>","bookmark-plus":"<path d=\"M12 7v6\"/><path d=\"M15 10H9\"/><path d=\"M17 3a2 2 0 0 1 2 2v15a1 1 0 0 1-1.496.868l-4.512-2.578a2 2 0 0 0-1.984 0l-4.512 2.578A1 1 0 0 1 5 20V5a2 2 0 0 1 2-2z\"/>","book-open-text":"<path d=\"M12 5v16\"/><path d=\"M16 13h2\"/><path d=\"M16 9h2\"/><path d=\"M20.001 19A2 2 0 0022 17V5a2 2 0 00-1.999-2L16 3.002A5 5 0 0012 5a5 5 0 00-4-2H4a2 2 0 00-2 2v12a2 2 0 001.999 2H8a5 5 0 014 2 5 5 0 014-2z\"/><path d=\"M6 13h2\"/><path d=\"M6 9h2\"/>","calendar-clock":"<path d=\"M16 14v2.2l1.6 1\"/><path d=\"M16 2v3\"/><path d=\"M21 7.338V5a2 2 0 00-2-2H5a2 2 0 00-2 2v14a2 2 0 002 2h2.338\"/><path d=\"M3 9h5.859\"/><path d=\"M8 2v3\"/><circle cx=\"16\" cy=\"16\" r=\"6\"/>","chevron-left":"<path d=\"m15 18-6-6 6-6\"/>","eye-off":"<path d=\"M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49\"/><path d=\"M14.084 14.158a3 3 0 0 1-4.242-4.242\"/><path d=\"M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143\"/><path d=\"m2 2 20 20\"/>","file-pen":"<path d=\"M12.659 22H18a2 2 0 0 0 2-2V8a2.4 2.4 0 0 0-.706-1.706l-3.588-3.588A2.4 2.4 0 0 0 14 2H6a2 2 0 0 0-2 2v9.34\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><path d=\"M10.378 12.622a1 1 0 0 1 3 3.003L8.36 20.637a2 2 0 0 1-.854.506l-2.867.837a.5.5 0 0 1-.62-.62l.836-2.869a2 2 0 0 1 .506-.853z\"/>","file-question":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M12 17h.01\"/><path d=\"M9.1 9a3 3 0 0 1 5.82 1c0 2-3 3-3 3\"/>","file-x":"<path d=\"M6 22a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h8a2.4 2.4 0 0 1 1.704.706l3.588 3.588A2.4 2.4 0 0 1 20 8v12a2 2 0 0 1-2 2z\"/><path d=\"M14 2v5a1 1 0 0 0 1 1h5\"/><path d=\"m14.5 12.5-5 5\"/><path d=\"m9.5 12.5 5 5\"/>","folder-input":"<path d=\"M2 9V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H20a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-1\"/><path d=\"M2 13h10\"/><path d=\"m9 16 3-3-3-3\"/>","folder-open":"<path d=\"m6 14 1.5-2.9A2 2 0 0 1 9.24 10H20a2 2 0 0 1 1.94 2.5l-1.54 6a2 2 0 0 1-1.95 1.5H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h3.9a2 2 0 0 1 1.69.9l.81 1.2a2 2 0 0 0 1.67.9H18a2 2 0 0 1 2 2v2\"/>","link-2":"<path d=\"M9 17H7A5 5 0 0 1 7 7h2\"/><path d=\"M15 7h2a5 5 0 1 1 0 10h-2\"/><line x1=\"8\" x2=\"16\" y1=\"12\" y2=\"12\"/>","list-plus":"<path d=\"M16 5H3\"/><path d=\"M11 12H3\"/><path d=\"M16 19H3\"/><path d=\"M18 9v6\"/><path d=\"M21 12h-6\"/>","mic":"<path d=\"M12 19v3\"/><path d=\"M19 10v2a7 7 0 0 1-14 0v-2\"/><rect x=\"9\" y=\"2\" width=\"6\" height=\"13\" rx=\"3\"/>","plug":"<path d=\"M12 22v-5\"/><path d=\"M15 8V2\"/><path d=\"M17 8a1 1 0 0 1 1 1v4a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V9a1 1 0 0 1 1-1z\"/><path d=\"M9 8V2\"/>","puzzle":"<path d=\"M15.39 4.39a1 1 0 0 0 1.68-.474 2.5 2.5 0 1 1 3.014 3.015 1 1 0 0 0-.474 1.68l1.683 1.682a2.414 2.414 0 0 1 0 3.414L19.61 15.39a1 1 0 0 1-1.68-.474 2.5 2.5 0 1 0-3.014 3.015 1 1 0 0 1 .474 1.68l-1.683 1.682a2.414 2.414 0 0 1-3.414 0L8.61 19.61a1 1 0 0 0-1.68.474 2.5 2.5 0 1 1-3.014-3.015 1 1 0 0 0 .474-1.68l-1.683-1.682a2.414 2.414 0 0 1 0-3.414L4.39 8.61a1 1 0 0 1 1.68.474 2.5 2.5 0 1 0 3.014-3.015 1 1 0 0 1-.474-1.68l1.683-1.682a2.414 2.414 0 0 1 3.414 0z\"/>","send":"<path d=\"M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z\"/><path d=\"m21.854 2.147-10.94 10.939\"/>","square-check":"<rect width=\"18\" height=\"18\" x=\"3\" y=\"3\" rx=\"2\"/><path d=\"m16 9-5.5 5.5L8 12\"/>","tags":"<path d=\"M13.172 2a2 2 0 0 1 1.414.586l6.71 6.71a2.4 2.4 0 0 1 0 3.408l-4.592 4.592a2.4 2.4 0 0 1-3.408 0l-6.71-6.71A2 2 0 0 1 6 9.172V3a1 1 0 0 1 1-1z\"/><path d=\"M2 7v6.172a2 2 0 0 0 .586 1.414l6.71 6.71a2.4 2.4 0 0 0 3.191.193\"/><circle cx=\"10.5\" cy=\"6.5\" r=\".5\" fill=\"currentColor\"/>","undo-2":"<path d=\"M9 14 4 9l5-5\"/><path d=\"M4 9h10.5a5.5 5.5 0 0 1 5.5 5.5a5.5 5.5 0 0 1-5.5 5.5H11\"/>","user-plus":"<path d=\"M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2\"/><circle cx=\"9\" cy=\"7\" r=\"4\"/><line x1=\"19\" x2=\"19\" y1=\"8\" y2=\"14\"/><line x1=\"22\" x2=\"16\" y1=\"11\" y2=\"11\"/>","user-round":"<circle cx=\"12\" cy=\"8\" r=\"5\"/><path d=\"M20 21a8 8 0 0 0-16 0\"/>","minus":"<path d=\"M5 12h14\"/>","circle":"<circle cx=\"12\" cy=\"12\" r=\"10\"/>","hourglass":"<path d=\"M5 22h14\"/><path d=\"M5 2h14\"/><path d=\"M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22\"/><path d=\"M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2\"/>","octagon-x":"<path d=\"m15 9-6 6\"/><path d=\"M2.586 16.726A2 2 0 0 1 2 15.312V8.688a2 2 0 0 1 .586-1.414l4.688-4.688A2 2 0 0 1 8.688 2h6.624a2 2 0 0 1 1.414.586l4.688 4.688A2 2 0 0 1 22 8.688v6.624a2 2 0 0 1-.586 1.414l-4.688 4.688a2 2 0 0 1-1.414.586H8.688a2 2 0 0 1-1.414-.586z\"/><path d=\"m9 9 6 6\"/>","import":"<path d=\"M12 3v12\"/><path d=\"m8 11 4 4 4-4\"/><path d=\"M8 5H4a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-4\"/>","calendar":"<path d=\"M8 2v3\"/><path d=\"M16 2v3\"/><rect x=\"3\" y=\"3\" width=\"18\" height=\"18\" rx=\"2\"/><path d=\"M3 9h18\"/>","headphones":"<path d=\"M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3\"/>"}};

const UI = "https://themightytrex.github.io/design-system/penpot/ui.html";
const THEME = "Light"; // Components use the Light colours; the other themes are in the library and Foundations.

penpot.ui.open("TRex Design System", `${UI}?theme=${penpot.theme}`, { width: 380, height: 600 });

/** @param {Record<string, unknown>} message */
const tell = (message) => penpot.ui.sendMessage(message);
const pause = () => new Promise((done) => setTimeout(done, 30));

penpot.ui.onMessage(async (/** @type {{type: string}} */ message) => {
  if (message.type === "build") await build();
  if (message.type === "close") penpot.closePlugin();
});

// Fonts, colours and the small builders every part uses ---------------------------------------------------

/** @type {Font | null} */
let font = null;

function findFont() {
  for (const name of [DATA.font, "Atkinson Hyperlegible", "Source Sans Pro"]) {
    const found = penpot.fonts.findByName(name);
    if (found) return found;
  }
  return null;
}

/** @param {string} weight */
function variantFor(weight) {
  if (!font) return undefined;
  const upright = font.variants.filter((v) => v.fontStyle !== "italic");
  return upright.find((v) => v.fontWeight === weight)
    || upright.sort((a, b) => Math.abs(Number(a.fontWeight) - Number(weight)) - Math.abs(Number(b.fontWeight) - Number(weight)))[0];
}

/** @type {Map<string, LibraryColor>} */
const libraryColours = new Map();

/** @param {string} name a colour role without its dashes, such as "color-accent" or "status-danger-fg" */
function fill(name, theme = THEME) {
  const shared = libraryColours.get(`${theme}/${name}`);
  if (shared) return shared.asFill();
  const c = DATA.themes[theme][name];
  return { fillColor: c ? c.hex : "#ff00ff", fillOpacity: c ? c.opacity : 1 };
}

/** @param {string} name @param {number} width */
function stroke(name, width = 1, theme = THEME) {
  const shared = libraryColours.get(`${theme}/${name}`);
  const s = shared ? shared.asStroke() : { strokeColor: DATA.themes[theme][name]?.hex || "#ff00ff", strokeOpacity: 1 };
  return { ...s, strokeWidth: width, strokeAlignment: /** @type {"inner"} */ ("inner"), strokeStyle: /** @type {"solid"} */ ("solid") };
}

/**
 * @param {string} characters
 * @param {{size?: number, weight?: number, colour?: string, typography?: LibraryTypography}} [o]
 */
function text(characters, o = {}) {
  const t = penpot.createText(characters);
  if (!t) throw new Error(`Penpot did not make the text "${characters}"`);
  if (o.typography) t.applyTypography(o.typography);
  else {
    if (font) font.applyToText(t, variantFor(String(o.weight || 400)));
    t.fontSize = String(o.size || DATA.core.text["text-md"]);
    t.lineHeight = "1.4";
  }
  t.fills = [fill(o.colour || "color-text")];
  t.growType = "auto-width";
  t.name = characters.length > 40 ? characters.slice(0, 40) : characters;
  return t;
}

/**
 * A board with flex layout. Sizes: a number is fixed; "hug" fits the content.
 * @param {string} name
 * @param {{dir?: "row" | "column", gap?: number, padX?: number, padY?: number, pad?: [number, number, number, number],
 *  w?: number | "hug", h?: number | "hug", fill?: string | null, stroke?: [string, number] | null,
 *  align?: "start" | "center" | "end" | "stretch", justify?: "start" | "center" | "end" | "space-between", wrap?: boolean}} [o]
 */
function box(name, o = {}) {
  const b = penpot.createBoard();
  b.name = name;
  b.fills = o.fill ? [fill(o.fill)] : [];
  b.strokes = o.stroke ? [stroke(o.stroke[0], o.stroke[1])] : [];
  b.clipContent = false;
  const w = o.w ?? "hug", h = o.h ?? "hug";
  b.resize(typeof w === "number" ? w : 100, typeof h === "number" ? h : 100);
  const flex = b.addFlexLayout();
  flex.dir = o.dir || "row";
  flex.wrap = o.wrap ? "wrap" : "nowrap";
  flex.alignItems = o.align || "center";
  flex.justifyContent = o.justify || "start";
  flex.rowGap = o.gap ?? 0;
  flex.columnGap = o.gap ?? 0;
  const [top, right, bottom, left] = o.pad || [o.padY ?? 0, o.padX ?? 0, o.padY ?? 0, o.padX ?? 0];
  flex.topPadding = top; flex.rightPadding = right; flex.bottomPadding = bottom; flex.leftPadding = left;
  // Penpot accepts "auto" (fits the content), "fix" and "fill", whatever its published types say.
  flex.horizontalSizing = /** @type {any} */ (w === "hug" ? "auto" : "fix");
  flex.verticalSizing = /** @type {any} */ (h === "hug" ? "auto" : "fix");
  return b;
}

/** @param {Board} parent @param {...Shape} children */
function add(parent, ...children) {
  for (const child of children) {
    if (parent.flex) parent.flex.appendChild(child);
    else parent.appendChild(child);
  }
  return parent;
}

/** @param {string} name @param {number} size @param {string} colour */
function icon(name, size = DATA.core.size["icon-md"], colour = "color-text") {
  const c = DATA.themes[THEME][colour];
  const body = DATA.icons[name];
  if (!body) throw new Error(`No icon called ${name}`);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="${c ? c.hex : "#000000"}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">${body}</svg>`;
  const g = penpot.createShapeFromSvg(svg);
  if (!g) throw new Error(`Penpot did not read the icon ${name}`);
  g.name = name;
  g.resize(size, size);
  return g;
}

/** @param {number} w @param {number} h @param {string} colour */
function rect(w, h, colour) {
  const r = penpot.createRectangle();
  r.resize(w, h);
  r.fills = [fill(colour)];
  return r;
}

/**
 * Makes a shape a library component, then puts its main copy in a row of the page.
 * @param {Shape} shape @param {string} path @param {string} name @param {Board} row
 */
function component(shape, path, name, row) {
  shape.name = name;
  const c = penpot.library.local.createComponent([shape]);
  c.name = name;
  c.path = path;
  const main = c.mainInstance();
  if (main && row) add(row, main);
  return c;
}

// Pages -----------------------------------------------------------------------------------------------------

/** @param {string} name */
async function newPage(name) {
  const page = penpot.createPage();
  page.name = name;
  penpot.openPage(page);
  await pause();
  return page;
}

/** A section on a page: a heading, a line of words, and a row for the items. @param {string} title @param {string} about */
function section(title, about, rowOptions = {}) {
  const s = box(title, { dir: "column", gap: 16, pad: [32, 32, 32, 32], w: 1280, fill: "color-bg", align: "start" });
  add(s, text(title, { size: DATA.core.text["text-xl"], weight: 700 }));
  if (about) add(s, text(about, { size: DATA.core.text["text-sm"], colour: "color-text-muted" }));
  const row = box(`${title} items`, { gap: 16, wrap: true, w: 1216, align: "start", ...rowOptions });
  add(s, row);
  return { s, row };
}

/** Stacks the sections of a page one under another. @param {Board[]} sections */
function stack(sections) {
  let y = 0;
  for (const s of sections) {
    s.x = 0;
    s.y = y;
    y += s.height + 40;
  }
}

// The parts --------------------------------------------------------------------------------------------------

function buildColours() {
  const lib = penpot.library.local;
  let count = 0;
  for (const [theme, colours] of Object.entries(DATA.themes)) {
    for (const [name, c] of Object.entries(colours)) {
      const lc = lib.createColor();
      lc.name = name;
      lc.path = theme;
      lc.color = c.hex;
      lc.opacity = c.opacity;
      libraryColours.set(`${theme}/${name}`, lc);
      count++;
    }
  }
  return `${count} colours in ${Object.keys(DATA.themes).length} themes`;
}

/** @type {Record<string, LibraryTypography>} */
const typographies = {};

function buildTypographies() {
  const t = DATA.core.text;
  const styles = [
    ["Heading 1", t["text-2xl"], "700", "1.25"], ["Heading 2", t["text-xl"], "700", "1.25"],
    ["Heading 3", t["text-lg"], "700", "1.3"], ["Lead", t["text-lg"], "400", "1.5"],
    ["Body", t["text-md"], "400", "1.5"], ["Body strong", t["text-md"], "600", "1.5"],
    ["Small", t["text-sm"], "400", "1.5"], ["Label", t["text-sm"], "600", "1.4"],
    ["Caption", t["text-xs"], "600", "1.4"],
  ];
  for (const [name, size, weight, lineHeight] of styles) {
    const ty = penpot.library.local.createTypography();
    ty.name = String(name);
    ty.path = "Text";
    if (font) ty.setFont(font, variantFor(String(weight)));
    ty.fontSize = String(size);
    ty.fontWeight = String(weight);
    ty.lineHeight = String(lineHeight);
    ty.letterSpacing = "0";
    typographies[String(name)] = ty;
  }
  return `${styles.length} text styles in ${font ? font.name : "Penpot's default font"}`;
}

async function buildCover() {
  await newPage("Cover");
  const c = box("Cover", { dir: "column", gap: 16, pad: [64, 64, 64, 64], w: 1280, h: 720, fill: "color-bg", align: "start", justify: "center" });
  add(c,
    text("TRex Design System", { typography: typographies["Heading 1"] }),
    text("One design system for Storyarr and Starboard: tokens, components, icons and guides.", { typography: typographies.Lead }),
    text("Built by the TRex Design System plugin from the library at github.com/TheMightyTRex/design-system.", { typography: typographies.Small, colour: "color-text-muted" }),
    text("Every colour meets WCAG 2.2 AA in all four themes. Change the library there, then run the plugin again in a new file.", { typography: typographies.Small, colour: "color-text-muted" }));
  c.x = 0; c.y = 0;
  return "1 board";
}

async function buildFoundations() {
  await newPage("Foundations");
  const sections = [];
  for (const [theme, colours] of Object.entries(DATA.themes)) {
    const { s, row } = section(`Colour: ${theme}`, `The ${theme} theme. Components use role names, never a raw colour.`, { gap: 12 });
    for (const name of Object.keys(colours)) {
      const card = box(name, { dir: "column", gap: 4, w: 172, align: "start" });
      const sw = rect(172, 48, "color-bg");
      sw.fills = [fill(name, theme)];
      sw.strokes = [stroke("color-divider")];
      add(card, sw, text(name, { size: 12, weight: 600 }),
        text(`${colours[name].hex}${colours[name].opacity < 1 ? ` at ${Math.round(colours[name].opacity * 100)}%` : ""}`, { size: 12, colour: "color-text-muted" }));
      add(row, card);
    }
    sections.push(s);
    await pause();
  }
  const type = section("Type", `${font ? font.name : "The default font"}, one typeface at five sizes. Text scales with the Text size setting in each app.`, { dir: "column", gap: 12 });
  for (const [name, ty] of Object.entries(typographies)) add(type.row, text(`${name}: the lighthouse keeper's niece`, { typography: ty }));
  sections.push(type.s);
  const space = section("Space and size", "Space on a 4px scale. Controls and targets are 44px; 32px only in dense tables.", { dir: "column", gap: 8 });
  for (const [name, v] of Object.entries(DATA.core.space)) {
    const line = box(name, { gap: 12 });
    add(line, rect(v, 16, "color-accent"), text(`${name}: ${v}px`, { size: 14 }));
    add(space.row, line);
  }
  for (const [name, v] of Object.entries(DATA.core.size)) add(space.row, text(`${name}: ${v}px`, { size: 14, colour: "color-text-muted" }));
  sections.push(space.s);
  stack(sections);
  return `${sections.length} sections`;
}

async function buildIcons() {
  await newPage("Icons");
  const { s, row } = section("Icons", "Lucide icons at 24px with a 2px stroke. Beside words they are decorative; alone, the control carries the name.", { gap: 8 });
  let count = 0;
  for (const name of Object.keys(DATA.icons)) {
    const cell = box(`${name} cell`, { dir: "column", gap: 6, w: 112, padY: 8, align: "center" });
    add(row, cell);
    const c = component(icon(name, 24), "Icons", name, cell);
    add(cell, text(name, { size: 11, colour: "color-text-muted" }));
    if (c) count++;
    if (count % 20 === 0) await pause();
  }
  stack([s]);
  return `${count} icon components`;
}

/** @param {"default" | "primary" | "quiet" | "danger"} kind @param {string} label @param {string | null} iconName */
function button(kind, label, iconName = null, compact = false) {
  const colours = {
    default: ["color-surface", "color-border", "color-text"],
    primary: ["color-accent", "color-accent", "color-accent-text"],
    quiet: [null, null, "color-accent"],
    danger: ["color-surface", "status-danger-fg", "status-danger-fg"],
  }[kind];
  const b = box(label, { gap: 8, padX: compact ? 12 : 16, h: compact ? DATA.core.size["control-h-compact"] : DATA.core.size["control-h"],
    fill: colours[0], stroke: colours[1] ? [colours[1], 1] : null, justify: "center" });
  const ink = colours[2] || "color-text";
  if (iconName) add(b, icon(iconName, DATA.core.size["icon-md"], ink));
  add(b, text(label, { typography: typographies.Label, colour: ink }));
  return b;
}

const TONES = {
  success: ["circle-check", "In library"], info: ["info", "Downloading"], warning: ["triangle-alert", "Needs attention"],
  danger: ["circle-x", "Failed"], neutral: ["clock", "Waiting"], muted: ["circle", "Excluded"],
};

async function buildComponents() {
  await newPage("Components");
  const sections = [];
  let count = 0;

  const buttons = section("Buttons", "44px high, square, bold small text. One primary button per view; the words say what happens.");
  for (const [kind, label, ic] of /** @type {const} */ ([["primary", "Save changes", null], ["default", "Search now", "search"], ["quiet", "Cancel", null], ["danger", "Delete book", "trash-2"]])) {
    component(button(kind, label, ic), "Buttons", kind[0].toUpperCase() + kind.slice(1), buttons.row); count++;
  }
  component(button("default", "Search now", null, true), "Buttons", "Compact", buttons.row); count++;
  const ib = box("Icon button", { w: 44, h: 44, stroke: ["color-border", 1], justify: "center" });
  add(ib, icon("ellipsis"));
  component(ib, "Buttons", "Icon button", buttons.row); count++;
  sections.push(buttons.s);
  await pause();

  const chips = section("Status chips", "A word, an icon and a colour together, so status never rests on colour alone.");
  for (const [tone, [ic, word]] of Object.entries(TONES)) {
    const fg = `status-${tone}-fg`;
    const chip = box(word, { gap: 4, padX: 8, h: 24, fill: "color-surface", stroke: [fg, 1] });
    add(chip, icon(ic, 14, fg), text(word, { typography: typographies.Caption, colour: fg }));
    component(chip, "Status chips", tone[0].toUpperCase() + tone.slice(1), chips.row); count++;
  }
  const tag = box("Tag", { gap: 4, padX: 8, h: 24, stroke: ["color-divider", 1] });
  add(tag, text("Audiobook", { typography: typographies.Caption, colour: "color-text-muted" }));
  component(tag, "Status chips", "Tag", chips.row); count++;
  sections.push(chips.s);
  await pause();

  const notices = section("Notices and callouts", "The lead word says the meaning, so it never rests on colour.", { dir: "column", gap: 12 });
  const leads = { info: ["info", "Before you begin:", "You need the server address and an API key."], success: ["circle-check", "Tip:", "Select a row to open its details."],
    warning: ["triangle-alert", "Limitation:", "Storyarr does not import ebooks from Calibre."], danger: ["circle-alert", "Warning:", "Deleting a book cannot be undone."] };
  for (const [tone, [ic, title, body]] of Object.entries(leads)) {
    const fg = `status-${tone}-fg`;
    const n = box(title, { w: 560, fill: `status-${tone}-bg`, align: "stretch" });
    const edge = rect(4, 40, fg);
    add(n, edge);
    if (edge.layoutChild) edge.layoutChild.verticalSizing = "fill";
    const inner = box("Content", { gap: 12, padX: 16, padY: 12, align: "start" });
    const words = box("Words", { dir: "column", gap: 4, align: "start" });
    add(words, text(title, { typography: typographies.Label, colour: fg }), text(body, { typography: typographies.Small, colour: fg }));
    add(inner, icon(ic, DATA.core.size["icon-md"], fg), words);
    add(n, inner);
    component(n, "Notices", tone[0].toUpperCase() + tone.slice(1), notices.row); count++;
  }
  const toast = box("Toast", { w: 360, fill: "color-surface-raised", stroke: ["color-border", 1], align: "stretch" });
  const tEdge = rect(DATA.core.size["status-edge-w"], 40, "status-success-fg");
  add(toast, tEdge);
  if (tEdge.layoutChild) tEdge.layoutChild.verticalSizing = "fill";
  const tInner = box("Content", { gap: 12, padX: 12, padY: 12, align: "start" });
  const tWords = box("Words", { dir: "column", gap: 2, align: "start" });
  add(tWords, text("Follow saved", { typography: typographies.Label }), text("New books by Mara Ellison come in by themselves", { typography: typographies.Small, colour: "color-text-muted" }));
  add(tInner, icon("circle-check", DATA.core.size["icon-md"], "status-success-fg"), tWords, icon("x", 16, "color-text-muted"));
  add(toast, tInner);
  component(toast, "Notices", "Toast", notices.row); count++;
  sections.push(notices.s);
  await pause();

  const inputs = section("Inputs", "A visible label above every control, a hint when needed, and an error that says how to fix it.", { gap: 32 });
  /** @param {boolean} error */
  const field = (error) => {
    const f = box(error ? "Field with error" : "Field", { dir: "column", gap: 4, w: 320, align: "stretch" });
    add(f, text("Server address", { typography: typographies.Label }), text("Include the port, such as :8080.", { typography: typographies.Small, colour: "color-text-muted" }));
    const input = box("Input", { padX: 12, h: DATA.core.size["control-h"], fill: "color-surface-raised", stroke: error ? ["status-danger-fg", 2] : ["color-border", 1] });
    add(input, text(error ? "qbittorrent" : "http://qbittorrent.example:8080", { typography: typographies.Body }));
    add(f, input);
    if (input.layoutChild) input.layoutChild.horizontalSizing = "fill";
    if (error) {
      const e = box("Error", { gap: 4 });
      add(e, icon("circle-alert", 16, "status-danger-fg"), text("Enter an address that starts with http:// or https://", { typography: typographies.Label, colour: "status-danger-fg" }));
      add(f, e);
    }
    return f;
  };
  component(field(false), "Inputs", "Field", inputs.row); count++;
  component(field(true), "Inputs", "Field with error", inputs.row); count++;
  /** @param {boolean} on */
  const check = (on) => {
    const c = box(on ? "Checkbox, selected" : "Checkbox", { gap: 12, h: DATA.core.size["control-h"] });
    const tick = box("Box", { w: 22, h: 22, fill: on ? "color-accent" : "color-surface-raised", stroke: [on ? "color-accent" : "color-border", 2], justify: "center" });
    if (on) add(tick, icon("check", 16, "color-accent-text"));
    add(c, tick, text("Include audiobooks", { typography: typographies.Body }));
    return c;
  };
  component(check(false), "Inputs", "Checkbox", inputs.row); count++;
  component(check(true), "Inputs", "Checkbox selected", inputs.row); count++;
  /** @param {boolean} on */
  const toggle = (on) => {
    const s = box(on ? "Switch, active" : "Switch", { gap: 16, h: DATA.core.size["control-h"] });
    const track = box("Track", { w: 44, h: 24, padX: 3, fill: on ? "color-accent" : "color-surface-sunken", stroke: [on ? "color-accent" : "color-border", 1], justify: on ? "end" : "start" });
    add(track, rect(16, 16, on ? "color-accent-text" : "color-border"));
    add(s, text("Upgrade automatically", { typography: typographies.Body }), track);
    return s;
  };
  component(toggle(false), "Inputs", "Switch", inputs.row); count++;
  component(toggle(true), "Inputs", "Switch active", inputs.row); count++;
  const seg = box("Segmented", { stroke: ["color-border", 1] });
  ["Light", "Dark", "Match device"].forEach((label, i) => {
    const part = box(label, { padX: 12, h: DATA.core.size["control-h"], fill: i === 0 ? "color-accent" : null, justify: "center" });
    add(part, text(label, { typography: typographies.Label, colour: i === 0 ? "color-accent-text" : "color-text" }));
    add(seg, part);
  });
  component(seg, "Inputs", "Segmented", inputs.row); count++;
  sections.push(inputs.s);
  await pause();

  const containers = section("Containers", "A card is one thing, and the whole card opens it.");
  const card = box("Card", { dir: "column", gap: 8, w: 320, padX: 16, padY: 16, fill: "color-surface", stroke: ["color-divider", 1], align: "start" });
  add(card, text("The Glass Harbour", { typography: typographies["Body strong"] }), text("Mara Ellison · Book 2 of The Glass Harbour", { typography: typographies.Small, colour: "color-text-muted" }));
  const cardChip = box("In library", { gap: 4, padX: 8, h: 24, fill: "color-surface", stroke: ["status-success-fg", 1] });
  add(cardChip, icon("circle-check", 14, "status-success-fg"), text("In library", { typography: typographies.Caption, colour: "status-success-fg" }));
  add(card, cardChip);
  component(card, "Containers", "Card", containers.row); count++;
  sections.push(containers.s);

  stack(sections);
  return `${count} components`;
}

// The run ----------------------------------------------------------------------------------------------------

async function build() {
  font = findFont();
  tell({ type: "font", name: font ? font.name : null });
  const steps = [
    ["Colours", buildColours], ["Text styles", buildTypographies], ["Cover", buildCover],
    ["Foundations", buildFoundations], ["Icons", buildIcons], ["Components", buildComponents],
  ];
  let failed = 0;
  for (const [label, run] of steps) {
    tell({ type: "step", label, status: "working" });
    try {
      const detail = await /** @type {() => Promise<string> | string} */ (run)();
      tell({ type: "step", label, status: "done", detail });
    } catch (error) {
      failed++;
      tell({ type: "step", label, status: "failed", detail: error instanceof Error ? error.message : String(error) });
    }
    await pause();
  }
  tell({ type: "finished", failed });
}
