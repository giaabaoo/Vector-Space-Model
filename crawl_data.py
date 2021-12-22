crawl_list = ["https://www.newscientist.com/article/2302492-fossilised-dinosaur-embryo-found-exquisitely-preserved-inside-egg/",
              "https://www.newscientist.com/article/2302484-fossil-of-the-largest-millipede-that-ever-lived-found-on-english-beach/",
              "https://www.newscientist.com/article/2302337-tardigrade-is-first-multicellular-organism-to-be-quantum-entangled/",
              "https://www.newscientist.com/article/mg23030713-100-how-is-helping-children-with-autism-make-new-friends/",
              "https://www.newscientist.com/article/2302438-remarkable-trove-of-species-found-living-beneath-antarctic-ice-shelf/",
              "https://www.newscientist.com/article/2302484-fossil-of-the-largest-millipede-that-ever-lived-found-on-english-beach/",
              "https://www.newscientist.com/article/2302450-higher-us-welfare-benefits-seem-to-protect-childrens-brains/",
              "https://www.newscientist.com/article/mg25233654-000-what-doing-magic-tricks-for-birds-is-revealing-about-animal-minds/",
              "https://www.newscientist.com/article/mg25233652-000-2021-in-review-jian-wei-pan-leads-chinas-quantum-computing-successes/",
              "https://www.newscientist.com/article/2302421-sample-of-asteroid-ryugu-brought-to-earth-is-a-strange-dark-colour/"]

import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os

Path("./news_data").mkdir(parents=True, exist_ok=True)

count = 0
for url in crawl_list:
  response = requests.get(url)
  doc_name = "doc" + str(count) + ".txt"
  count += 1

  soup = BeautifulSoup(response.text, 'html.parser')

  with open(os.path.join("./news_data/", doc_name), "w") as f:
    for data in soup.find_all("p"):
      s = data.get_text()
      f.write(s)