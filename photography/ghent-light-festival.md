---
layout: gallery
title: 速写/Sketches
no_menu_item: true # required only for this example website because of menu construction
support: [jquery, gallery]
---

想到什么画什么

{% include gallery-layout.html gallery=site.data.galleries.ghent-light-festival-1 id_number=1 %}

The pictures from part two:

{% include gallery-layout.html gallery=site.data.galleries.ghent-light-festival-2 id_number=2 %}

This is an example gallery. All images licensed under [CC-BY-NC-SA license][license]. Check the [Git Repo][repo] for a copy of this license.

[license]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[repo]: https://github.com/opieters/jekyll-gallery-example
