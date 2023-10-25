fpm \                                                                                                                                                                                          130 ⨯
  -s dir -t deb \
  -p markup-0.1.0-1-any.deb \
  --name markup \
  --version 0.1.0 \
  --architecture all \
  --depends bash \
  --description "Markdown Parser" \
  --url "https:/www.ayuge.top" \
  --maintainer "ayuge <ayuge.top>" -C markup .
