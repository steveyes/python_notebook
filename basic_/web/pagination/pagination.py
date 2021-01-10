from math import ceil, floor
from django.utils.safestring import mark_safe


class Page:
    def __init__(self, cur_page, total_items, n_items_display=10, n_index_labels=11):
        self.cur_page = cur_page
        self.total_items = total_items
        self.n_items_display = n_items_display
        self.n_index_labels = n_index_labels

    @property
    def start(self):
        return (self.cur_page - 1) * self.n_items_display

    @property
    def end(self):
        return self.cur_page * self.n_items_display

    @property
    def n_pages(self):
        v, y = divmod(self.total_items, self.n_items_display)
        v += 1 if y else 0
        return v

    def pager_reindex(self):

        half_n_index_labels = floor(self.n_index_labels / 2)

        if self.cur_page <= half_n_index_labels:
            start_index = 1
            end_index = min(self.n_index_labels, self.n_pages)
        elif self.cur_page + half_n_index_labels >= self.n_pages:
            end_index = self.n_pages
            start_index = end_index - self.n_index_labels + 1
        else:
            start_index = self.cur_page - half_n_index_labels
            end_index = self.cur_page + half_n_index_labels

        return int(start_index), int(end_index) + 1

    def url_build(self, url):
        page_bar = []
        start_index, end_index = self.pager_reindex()
        url_temp = '<a class="page {}" href="{}">{}</a>'

        if self.cur_page == 1:
            page_bar.append(url_temp.format('', 'javascript:void(0);', 'prev', ))
        else:
            page_bar.append(url_temp.format('', f'{url}{self.cur_page - 1}', 'prev'))

        for i in range(int(start_index), int(end_index)):
            if i == self.cur_page:
                page_bar.append(url_temp.format('active', f'{url}{i}', i))
            else:
                page_bar.append(url_temp.format('', f'{url}{i}', i))

        if self.cur_page == self.n_pages:
            page_bar.append(url_temp.format('', 'javascript:void(0);', 'next', ))
        else:
            # page_list.append(f'<a class="page" href="{url}{self.cur_page + 1}">next</a>')
            page_bar.append(url_temp.format('', f'{url}{self.cur_page + 1}', 'next', ))

        jump = """
        <input type='text'/><a onclick='jumpTo(this, "%s");'>GO</a>
        <script>
            function jumpTo(self,base){
                let val = self.previousSibling.value;
                location.href = base + val;
            }
        </script>
        """ % (url,)

        page_bar.append(jump)

        return mark_safe(" ".join(page_bar))
