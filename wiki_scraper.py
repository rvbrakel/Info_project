import wikipedia as wiki



wiki.set_lang('nl')


items = wiki.random(1000)

print(wiki.page(items[0]).content)







wiki.set_lang('fr')