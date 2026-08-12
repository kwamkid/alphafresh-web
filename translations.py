# Chinese (Simplified) and Arabic for every English string on the site.
# Keyed by the exact English text used in build.py's L() calls.
# A missing key simply falls back to English at render time.

TR = {
# ---- navigation, footer, shared ----
"Home": ("首页", "الرئيسية"),
"About": ("关于我们", "من نحن"),
"About us": ("关于我们", "من نحن"),
"Products": ("产品", "المنتجات"),
"Quality &amp; Export": ("品质与出口", "الجودة والتصدير"),
"Contact": ("联系我们", "اتصل بنا"),
"Company": ("公司", "الشركة"),
"How we work": ("作业流程", "طريقة عملنا"),
"Quality standards": ("质量标准", "معايير الجودة"),
"Target markets": ("目标市场", "الأسواق المستهدفة"),
"Request a quote": ("索取报价", "اطلب عرض سعر"),
"Request a quotation": ("索取报价", "اطلب عرض سعر"),
"See all products": ("查看全部产品", "عرض كل المنتجات"),
"Alpha Fresh Co., Ltd. — fresh fruit import &amp; export. Lamphun, Thailand.":
  ("Alpha Fresh 有限公司 — 泰国南奔府鲜果进出口商。",
   "شركة ألفا فريش — استيراد وتصدير الفواكه الطازجة، لامفون، تايلاند."),
"Figures on this draft site are illustrative placeholders.":
  ("本草稿网站上的部分数据仅为示例。", "الأرقام في هذه النسخة التجريبية توضيحية فقط."),
"Ready to order — or just want a price first?":
  ("准备下单，或者只想先问个价？", "جاهز للطلب — أم تريد السعر أولاً؟"),
"Tell us the fruit, the volume and the destination. You will get a price and a picking schedule back within two working days.":
  ("告诉我们水果种类、数量和目的地，我们会在两个工作日内回复价格和采摘排期。",
   "أخبرنا بنوع الفاكهة والكمية والوجهة، وسنرد بالسعر وجدول القطف خلال يومَي عمل."),

# ---- home: hero, stats ----
"Premium Thai Longan<span class='accent script'>from the orchard to your market</span>":
  ("泰国优质龙眼<span class='accent script'>从果园直达您的市场</span>",
   "لونجان تايلاندي فاخر<span class='accent script'>من البستان إلى سوقك</span>"),
"A small, hands-on packing house in Northern Thailand. Hand-graded, chilled within hours, and shipped with complete export paperwork — plus durian, mangosteen and lychee in season.":
  ("泰国北部一家亲力亲为的小型包装厂。人工分级，数小时内冷藏，出口单证齐全；应季还供应榴莲、山竹和荔枝。",
   "محطة فرز صغيرة في شمال تايلاند نديرها بأيدينا. فرز يدوي، تبريد خلال ساعات، وشحن بمستندات تصدير كاملة — إضافة إلى الدوريان والمانجوستين والليتشي في موسمها."),
"Products &amp; specifications": ("产品与规格", "المنتجات والمواصفات"),
"core export products": ("主要出口产品", "منتجات تصدير رئيسية"),
"GAP-certified partner orchards": ("GAP 认证合作果园", "بستان شريك حاصل على GAP"),
"orchard to airport": ("从果园到机场", "من البستان إلى المطار"),
"delivery terms available": ("可选交货条件", "شروط تسليم متاحة"),
"We started as importers — so we know what the buyer's end needs":
  ("我们从进口起家，因此清楚买家那一端真正在意什么",
   "بدأنا مستوردين — لذلك نعرف ما يحتاجه المشتري في الطرف الآخر"),
"Alpha Fresh began as a fruit importer. We already run the cold room, the refrigerated truck and a team fluent in customs clearance. Today we run it in reverse — the same chain, pointed outward — starting with what we know best: longan.":
  ("Alpha Fresh 起初是水果进口商。我们本就拥有冷库、冷藏车和熟悉清关的团队。如今我们把同一条链条反向运作，用于出口，从最擅长的龙眼开始。",
   "بدأت ألفا فريش كمستورد فواكه. لدينا أصلاً غرفة التبريد والشاحنة المبرّدة وفريق ملمّ بالتخليص الجمركي. واليوم نُشغّل السلسلة نفسها في الاتجاه المعاكس للتصدير، بدءاً بما نتقنه: اللونجان."),
"Read our story": ("了解我们的故事", "اقرأ قصتنا"),
"Our longan collection &amp; packing shed, Lamphun": ("我们位于南奔府的龙眼收购与包装场", "مركز التجميع والتعبئة في لامفون"),
"What we ship": ("我们出口什么", "ما نشحنه"),
"Longan first, and three more Thai fruits in season":
  ("以龙眼为主，另有三种应季泰国水果", "اللونجان أولاً، وثلاث فواكه تايلاندية أخرى في موسمها"),
"Fresh longan": ("新鲜龙眼", "لونجان طازج"),
"Monthong durian": ("金枕榴莲", "دوريان مونثونغ"),
"Monthong Durian": ("金枕榴莲", "دوريان مونثونغ"),
"Mangosteen": ("山竹", "مانجوستين"),
"Lychee": ("荔枝", "ليتشي"),
"E-Daw · Daw · Biew Kiew · grades AA–C · Jul–Sep plus off-season":
  ("依多 · 多 · 标绿 · AA–C 级 · 7–9月及反季", "إي‑داو · داو · بيو كيو · درجات AA–C · يوليو–سبتمبر وخارج الموسم"),
"Full specification": ("查看完整规格", "المواصفات الكاملة"),
"80–85% maturity · Apr–Aug": ("成熟度 80–85% · 4–8月", "نضج 80–85٪ · أبريل–أغسطس"),
"See details": ("查看详情", "التفاصيل"),
"Glossy rind, fresh calyx · May–Sep": ("果皮油亮、果蒂新鲜 · 5–9月", "قشرة لامعة وكأس أخضر · مايو–سبتمبر"),
"Hong Huay · Chakrapad · Apr–Jun": ("红辉 · 皇帝 · 4–6月", "هونغ هواي · جاكرابات · أبريل–يونيو"),
"Five steps, from first enquiry to departure": ("从询价到出运，五个步骤", "خمس خطوات، من الاستفسار حتى الشحن"),
"Enquiry": ("询价", "الاستفسار"),
"Fruit, grade, volume, destination and Incoterm.": ("水果种类、等级、数量、目的地和贸易术语。", "الصنف والدرجة والكمية والوجهة وشرط التسليم."),
"Sourcing": ("采购", "التوريد"),
"Harvest booked with GAP orchards, price and date fixed.": ("向 GAP 果园预订产量，锁定价格和采摘日期。", "حجز المحصول من بساتين GAP مع تثبيت السعر وتاريخ القطف."),
"Grading": ("分级", "الفرز"),
"Hand-graded, weighed, sealed and photographed for approval.": ("人工分级、称重、封箱，并拍照供确认。", "فرز يدوي ووزن وإغلاق وتصوير للاعتماد."),
"Documents": ("单证", "المستندات"),
"Phyto, C/O, invoice, packing list, B/L or AWB.": ("植检证、产地证、发票、装箱单、提单或空运单。", "شهادة صحة نباتية وشهادة منشأ وفاتورة وقائمة تعبئة وبوليصة شحن."),
"Shipping": ("出运", "الشحن"),
"Reefer container or air freight, with tracking sent.": ("冷藏柜或空运，并提供追踪信息。", "حاوية مبرّدة أو شحن جوي مع إرسال بيانات التتبع."),
"Quality standards and export terms": ("查看质量标准与出口条件", "معايير الجودة وشروط التصدير"),

# ---- about ----
"Where we come from": ("我们的起点", "من أين بدأنا"),
"A small business that still touches every crate": ("一家仍然亲手过目每一筐的小企业", "شركة صغيرة ما زالت تفحص كل صندوق بيدها"),
"Alpha Fresh began by importing fruit for the domestic market. That work taught us two things — where in the chain fruit actually spoils, and what buyers get frustrated about. So we know what must not slip when the fruit goes the other way.":
  ("Alpha Fresh 最初为国内市场进口水果。那段经历教会我们两件事：水果究竟在链条的哪一环变质，以及买家最容易为什么恼火。所以当货物反向出口时，我们清楚哪些环节绝不能出错。",
   "بدأت ألفا فريش باستيراد الفاكهة للسوق المحلي. علّمَنا ذلك أمرين: أين تفسد الفاكهة فعلياً داخل السلسلة، وما الذي يزعج المشترين. لذلك نعرف ما الذي يجب ألا يخطئ عندما تسير البضاعة في الاتجاه المعاكس."),
"Today we are a small sorting shed, not a large factory. Our lots are modest — which is exactly why we can still check crate by crate instead of sampling.":
  ("今天我们是一家小型分选场，而不是大工厂。我们的批量不大，正因如此才能逐筐检查，而不是抽检。",
   "نحن اليوم محطة فرز صغيرة، لا مصنع كبير. دفعاتنا متواضعة، ولهذا بالذات نستطيع فحص صندوق تلو الآخر بدل الاكتفاء بالعيّنات."),
"<b>Cold chain already in place</b> — our own cold room and refrigerated truck, no queueing for third parties.":
  ("<b>冷链现成可用</b> — 自有冷库和冷藏车，无需排队等外包。",
   "<b>سلسلة تبريد جاهزة</b> — غرفة تبريد وشاحنة مبرّدة مملوكتان لنا، دون انتظار طرف ثالث."),
"<b>Paperwork in-house</b> — phytosanitary certificate, C/O, packing list and invoice handled by one team.":
  ("<b>单证自办</b> — 植检证、产地证、装箱单和发票由同一团队处理。",
   "<b>المستندات داخلياً</b> — شهادة الصحة النباتية وشهادة المنشأ وقائمة التعبئة والفاتورة يتولاها فريق واحد."),
"<b>Small enough to check every crate</b> — hand-graded in modest lots, so quality control is real, not a claim.":
  ("<b>规模小到能查每一筐</b> — 小批量人工分级，品控是真的做，不是说说。",
   "<b>صغيرون بما يكفي لفحص كل صندوق</b> — فرز يدوي بدفعات محدودة، فرقابة الجودة فعلية لا ادعاء."),
"<b>Direct with the orchards</b> — no chain of middlemen, so price and picking date can be agreed in advance.":
  ("<b>直接对接果园</b> — 没有层层中间商，价格和采摘日期可以提前谈定。",
   "<b>تعامل مباشر مع البساتين</b> — بلا سلسلة وسطاء، فيمكن الاتفاق على السعر وتاريخ القطف مسبقاً."),
"What we handle ourselves": ("我们亲自负责的部分", "ما نتولاه بأنفسنا"),
"Three things we do not hand to anyone else": ("三件事我们绝不外包", "ثلاثة أمور لا نسلّمها لأحد"),
"Every lot is graded by hand — loose or bruised clusters pulled before boxing. No automated grading line: our lots are not large enough to justify one, and at this scale hands are more accurate.":
  ("每一批都由人工分级，散果和碰伤的果串在装箱前挑出。我们没有自动分选线：批量不足以摊平成本，而在这个规模上，人手更准。",
   "كل دفعة تُفرز يدوياً، وتُستبعد العناقيد المرتخية أو المرضوضة قبل التعبئة. لا خط فرز آلي: دفعاتنا لا تبرّره، وعلى هذا الحجم اليد أدقّ."),
"The cold room": ("冷库", "غرفة التبريد"),
"Fruit goes into the cold room on picking day — never left outside overnight. Temperatures are logged, and if the buyer asks we put a data logger in the container.":
  ("水果在采摘当天入冷库，绝不在户外过夜。温度全程记录，买家要求时我们会在柜内放置温度记录仪。",
   "تدخل الفاكهة غرفة التبريد يوم القطف، ولا تُترك في الخارج ليلاً. تُسجَّل درجات الحرارة، وعند طلب المشتري نضع مسجّل بيانات داخل الحاوية."),
"Documents and loading": ("单证与装柜", "المستندات والتحميل"),
"The same team that used to clear inbound shipments prepares the outbound papers. We are present at every loading, and send lot photos to the buyer before the container is sealed.":
  ("以前负责进口清关的同一批人，现在负责出口单证。每次装柜我们都在场，封柜前会把该批货的照片发给买家。",
   "الفريق نفسه الذي كان يخلّص الشحنات الواردة يجهّز مستندات التصدير. نحضر كل عملية تحميل، ونرسل صور الدفعة للمشتري قبل إغلاق الحاوية."),
"A partner orchard in Lamphun": ("南奔府的一处合作果园", "بستان شريك في لامفون"),
"Our orchards": ("我们的果园网络", "بساتيننا"),
"Twenty-odd orchards, and we know every owner": ("二十多个果园，每一位园主我们都认识", "أكثر من عشرين بستاناً، ونعرف كل مالك"),
"We do not buy through the central market. We book the harvest a season ahead with GAP-certified orchards, which lets us fix price and picking date in advance — and know which plot each lot came from.":
  ("我们不通过中央批发市场采购，而是提前一季向 GAP 认证果园预订产量，因此能事先确定价格和采摘日期，也知道每一批果来自哪一块地。",
   "لا نشتري عبر السوق المركزي، بل نحجز المحصول قبل موسم كامل من بساتين معتمدة بشهادة GAP، ما يتيح تثبيت السعر وتاريخ القطف مسبقاً ومعرفة القطعة التي أتت منها كل دفعة."),
"In season we draw from Lamphun, Chiang Mai and Chiang Rai; off-season fruit comes from induced orchards in Chanthaburi.":
  ("旺季货源来自南奔、清迈和清莱；反季则来自尖竹汶的催花果园。",
   "في الموسم نستقدم من لامفون وشيانغ ماي وشيانغ راي، وخارج الموسم من بساتين مُحفَّزة في جانثابوري."),
"The standards we work to": ("查看我们遵循的标准", "المعايير التي نعمل بها"),

# ---- products ----
"Flagship product": ("主力产品", "المنتج الرئيسي"),
"Fresh Longan (Dimocarpus longan)": ("新鲜龙眼（Dimocarpus longan）", "اللونجان الطازج (Dimocarpus longan)"),
"Longan from partner orchards in Lamphun, Chiang Mai and Chanthaburi. Hand-picked, de-stemmed, washed, SO₂-treated to destination requirement, and into the cold room the same day.":
  ("龙眼来自南奔、清迈和尖竹汶的合作果园。人工采摘、剪梗、清洗，按目的地要求做二氧化硫处理，当天入冷库。",
   "لونجان من بساتين شريكة في لامفون وشيانغ ماي وجانثابوري. يُقطف يدوياً ويُنزع عنقه ويُغسل ويُعالَج بثاني أكسيد الكبريت حسب اشتراطات الوجهة، ثم يدخل غرفة التبريد في اليوم نفسه."),
"Varieties": ("品种", "الأصناف"),
"E-Daw (main export variety) · Daw · Biew Kiew — thicker flesh, less sugary, suited to premium markets":
  ("依多（主力出口品种）· 多 · 标绿 — 果肉更厚、甜度较低，适合高端市场",
   "إي‑داو (صنف التصدير الرئيسي) · داو · بيو كيو — لبّ أسمك وحلاوة أقل، مناسب للأسواق الفاخرة"),
"Growing areas": ("产区", "مناطق الزراعة"),
"Lamphun · Chiang Mai · Chiang Rai (in season); Chanthaburi (off-season)":
  ("南奔 · 清迈 · 清莱（旺季）；尖竹汶（反季）", "لامفون · شيانغ ماي · شيانغ راي (الموسم)؛ جانثابوري (خارج الموسم)"),
"Season": ("季节", "الموسم"),
"In season Jul–Sep (peak August) · off-season Nov–Feb from induced orchards":
  ("旺季 7–9月（8月为高峰）· 反季 11–2月，来自催花果园",
   "الموسم يوليو–سبتمبر (الذروة أغسطس) · خارج الموسم نوفمبر–فبراير من بساتين مُحفَّزة"),
"Grades": ("等级", "الدرجات"),
"AA · A · B · C, graded by fruit diameter and cluster condition":
  ("AA · A · B · C，按果径和果串完整度分级", "AA · A · B · C، حسب قطر الثمرة وحالة العنقود"),
"Packing": ("包装", "التعبئة"),
"Plastic crates or cartons of 5 kg and 10 kg, lined with absorbent paper and a moisture pad · buyer's own branding available":
  ("5 公斤和 10 公斤塑料筐或纸箱，内衬吸水纸和保湿垫 · 可印买家品牌",
   "صناديق بلاستيكية أو كرتونية 5 و10 كغ، مبطّنة بورق ماص ولبادة رطوبة · إمكانية طباعة علامة المشتري"),
"Storage temperature": ("储运温度", "درجة حرارة التخزين"),
"2–5 °C at 90–95% relative humidity": ("2–5 °C，相对湿度 90–95%", "2–5 °م ورطوبة نسبية 90–95٪"),
"Shelf life": ("保鲜期", "مدة الصلاحية"),
"21–30 days with an unbroken cold chain": ("冷链不断的情况下 21–30 天", "21–30 يوماً مع سلسلة تبريد غير منقطعة"),
"Container load": ("每柜装量", "حمولة الحاوية"),
"Approx. 2,000 cartons (10 kg) per 40 ft reefer ≈ 20 tonnes":
  ("每 40 尺冷藏柜约 2,000 箱（10 公斤）≈ 20 吨", "نحو 2,000 كرتونة (10 كغ) لكل حاوية مبرّدة 40 قدماً ≈ 20 طناً"),
"Sea: one 40 ft container · Air: 500 kg (trial lots negotiable)":
  ("海运：1 个 40 尺柜 · 空运：500 公斤（试单可谈）", "بحراً: حاوية 40 قدماً · جواً: 500 كغ (دفعات تجريبية قابلة للتفاوض)"),
"Longan grades": ("龙眼等级", "درجات اللونجان"),
"26 mm and above": ("26 毫米以上", "26 مم فأكثر"),
"Full clusters, even skin. Premium retail and gift markets.":
  ("果串完整、果皮均匀，适合高端零售和礼品市场。", "عناقيد كاملة وقشرة متجانسة. لأسواق التجزئة الفاخرة والهدايا."),
"24–26 mm": ("24–26 毫米", "24–26 مم"),
"Our best-selling grade — balance of size and price.": ("最畅销的等级，大小与价格最平衡。", "درجتنا الأكثر مبيعاً — توازن بين الحجم والسعر."),
"22–24 mm": ("22–24 毫米", "22–24 مم"),
"Wholesale and wet-market volume.": ("适合批发和农贸市场的走量需求。", "للبيع بالجملة وأسواق الخضار."),
"Below 22 mm": ("22 毫米以下", "أقل من 22 مم"),
"Processing, drying and canning.": ("用于加工、烘干和罐头。", "للتصنيع والتجفيف والتعليب."),
"Other fruits": ("其他水果", "فواكه أخرى"),
"Seasonal Thai fruits": ("应季泰国水果", "فواكه تايلاندية موسمية"),
"Harvested at 80–85% maturity with dry-matter testing on every lot, then foam-netted against knocks.":
  ("在成熟度 80–85% 时采收，每批检测干物质含量，并套发泡网防碰撞。",
   "يُقطف عند نضج 80–85٪ مع فحص المادة الجافة لكل دفعة، ثم يُغلَّف بشبك إسفنجي ضد الصدمات."),
"Apr–Aug": ("4–8月", "أبريل–أغسطس"),
"15–18 kg carton": ("15–18 公斤纸箱", "كرتونة 15–18 كغ"),
"Temp": ("温度", "الحرارة"),
"Selected for glossy rind and a fresh green calyx, with no gamboge staining or impact damage.":
  ("挑选果皮油亮、果蒂青绿，无黄胶渗出、无碰压伤的果实。",
   "يُنتقى بقشرة لامعة وكأس أخضر طازج، دون تصمّغ أو ضرر ناتج عن الصدم."),
"May–Sep": ("5–9月", "مايو–سبتمبر"),
"5 / 10 kg carton": ("5 / 10 公斤纸箱", "كرتونة 5 / 10 كغ"),
"Hong Huay and Chakrapad, picked at dawn and chilled immediately — lychee browns faster than anything else we ship.":
  ("红辉和皇帝品种，清晨采摘后立即预冷 — 荔枝是我们出口的水果中褐变最快的。",
   "صنفا هونغ هواي وجاكرابات، يُقطفان فجراً ويُبرَّدان فوراً — فالليتشي أسرع ما نشحنه اسمراراً."),
"Apr–Jun": ("4–6月", "أبريل–يونيو"),
"2 / 5 kg carton, gel ice": ("2 / 5 公斤纸箱，附冰袋", "كرتونة 2 / 5 كغ مع ثلج جِل"),

# ---- harvest calendar ----
"Harvest calendar": ("产季日历", "روزنامة الحصاد"),
"When Thai fruit is in season": ("泰国水果的产季分布", "متى تكون الفواكه التايلاندية في موسمها"),
"Use it to plan when to book. The peak band is when volume is highest and the price is best — the first four are what we export ourselves; the rest are here to show the shape of the Thai fruit year.":
  ("用它来安排预订时间。深色为高峰期，产量最大、价格最好。前四种是我们自己出口的品项，其余列出以便了解泰国全年水果的节奏。",
   "استخدمها لتخطيط موعد الحجز. الشريط الداكن هو الذروة حيث الكمية أكبر والسعر أفضل — الأربعة الأولى نصدّرها بأنفسنا، والبقية لبيان إيقاع الفواكه التايلاندية على مدار السنة."),
"Swipe the table sideways for the later months": ("向右滑动查看后面的月份", "اسحب الجدول جانبياً لرؤية بقية الأشهر"),
"Peak — highest volume": ("高峰期 — 产量最大", "الذروة — أعلى كمية"),
"In season": ("产季", "في الموسم"),
"This month": ("当月", "هذا الشهر"),
"National averages. The North and the East run two to three weeks apart, and longan and mango also crop off-season from induced orchards.":
  ("为全国平均值。北部与东部相差约两到三周；龙眼和芒果另有催花反季产量。",
   "متوسطات وطنية. يفصل بين الشمال والشرق أسبوعان إلى ثلاثة، كما يُنتج اللونجان والمانجو خارج الموسم من بساتين مُحفَّزة."),
"Fruit": ("水果", "الفاكهة"),
"What we export": ("我们出口的品项", "ما نصدّره"),
"Other Thai fruit": ("其他泰国水果", "فواكه تايلاندية أخرى"),
"ours": ("自营", "لدينا"),
"Longan": ("龙眼", "لونجان"),
"Durian": ("榴莲", "دوريان"),
"Rambutan": ("红毛丹", "رامبوتان"),
"Longkong": ("龙贡果", "لونغكونغ"),
"Mango (Nam Dok Mai)": ("芒果（金煌/南多迈）", "مانجو (نام دوك ماي)"),
"Pomelo": ("柚子", "بوملي"),
"Dragon fruit": ("火龙果", "فاكهة التنين"),
"Jackfruit": ("菠萝蜜", "جاك فروت"),
"Pineapple": ("菠萝", "أناناس"),
"Young coconut": ("香水椰青", "جوز هند صغير"),
"Sweet tamarind": ("甜罗望子", "تمر هندي حلو"),

# ---- quality ----
"How an order runs": ("订单流程", "كيف يسير الطلب"),
"Tell us the fruit, grade, volume, destination and Incoterm. Quotation within two working days.":
  ("告诉我们水果种类、等级、数量、目的地和贸易术语，两个工作日内报价。",
   "أخبرنا بالصنف والدرجة والكمية والوجهة وشرط التسليم، ويصلك العرض خلال يومَي عمل."),
"We book the harvest with GAP orchards ahead of time, locking price and picking date.":
  ("我们提前向 GAP 果园预订产量，锁定价格和采摘日期。",
   "نحجز المحصول مسبقاً من بساتين GAP مع تثبيت السعر وتاريخ القطف."),
"Grading &amp; packing": ("分级与包装", "الفرز والتعبئة"),
"Hand-graded to the agreed spec, weighed, sealed — and photographed for your approval before loading.":
  ("按约定规格人工分级、称重、封箱，装柜前拍照供您确认。",
   "فرز يدوي حسب المواصفة المتفق عليها، ثم وزن وإغلاق وتصوير لاعتمادكم قبل التحميل."),
"Documentation": ("单证", "المستندات"),
"Phytosanitary certificate, C/O, invoice, packing list and B/L or AWB.":
  ("植检证、产地证、发票、装箱单，以及提单或空运单。",
   "شهادة صحة نباتية وشهادة منشأ وفاتورة وقائمة تعبئة وبوليصة شحن بحري أو جوي."),
"Reefer container or air freight, with tracking details sent every time.":
  ("冷藏柜或空运，每次都提供追踪信息。", "حاوية مبرّدة أو شحن جوي، مع إرسال بيانات التتبع في كل مرة."),
"Standards &amp; testing": ("标准与检测", "المعايير والفحوصات"),
"What we can guarantee — and what we do not claim": ("我们能保证什么，以及不会夸口什么", "ما نضمنه — وما لا ندّعيه"),
"Production standards": ("生产标准", "معايير الإنتاج"),
"Partner orchards are GAP-certified; the packing shed follows GMP and HACCP practice, with lot records traceable back to the orchard.":
  ("合作果园均通过 GAP 认证；包装场按 GMP 和 HACCP 规范作业，批次记录可追溯到具体果园。",
   "البساتين الشريكة معتمدة بشهادة GAP، ومحطة التعبئة تعمل وفق ممارسات GMP وHACCP، مع سجلات دفعات يمكن تتبعها حتى البستان."),
"Residues &amp; certificates": ("残留检测与证书", "المتبقيات والشهادات"),
"Residue testing against destination MRLs — EU, China (GACC) and Japan — with a phytosanitary certificate on every shipment.":
  ("按目的地最大残留限量检测 — 欧盟、中国（海关总署）和日本 — 每批出货均附植检证。",
   "فحص المتبقيات وفق الحدود القصوى للوجهة — الاتحاد الأوروبي والصين (GACC) واليابان — مع شهادة صحة نباتية لكل شحنة."),
"Cold chain": ("冷链", "سلسلة التبريد"),
"Into the cold room on picking day, temperature logged throughout, with a data logger placed in the container on request.":
  ("采摘当天入冷库，全程记录温度，可按要求在柜内放置温度记录仪。",
   "الدخول إلى غرفة التبريد يوم القطف، مع تسجيل الحرارة طوال الرحلة ووضع مسجّل بيانات في الحاوية عند الطلب."),
"Plainly stated": ("坦白说", "بصراحة"),
"We are a small business. There is no automated line and no in-house laboratory here — residue testing goes to an external lab, and there is a ceiling on what we can handle per week. If an order is beyond us, we will say so up front rather than take it and hope.":
  ("我们是小企业，这里没有自动化产线，也没有自己的实验室 — 残留检测送外部实验室，每周处理量也有上限。如果订单超出我们的能力，我们会一开始就说清楚，而不是先接下来再赌运气。",
   "نحن شركة صغيرة. لا يوجد خط آلي ولا مختبر داخلي — تُرسل فحوصات المتبقيات إلى مختبر خارجي، ولطاقتنا الأسبوعية سقف. وإن كان الطلب أكبر من قدرتنا، نقولها منذ البداية بدل قبوله والمراهنة على الحظ."),
"Terms": ("条件", "الشروط"),
"Delivery and payment": ("交货与付款", "التسليم والدفع"),
"Delivery terms (Incoterms 2020)": ("交货条件（Incoterms 2020）", "شروط التسليم (إنكوترمز 2020)"),
"collect at our shed in Lamphun": ("在南奔府我们的分选场自提", "الاستلام من محطتنا في لامفون"),
"Laem Chabang port, or Suvarnabhumi / Chiang Mai airport":
  ("林查班港，或素万那普 / 清迈机场", "ميناء لايم تشابانغ أو مطار سوفارنابومي / شيانغ ماي"),
"to the agreed destination port": ("至约定的目的港", "حتى ميناء الوجهة المتفق عليه"),
"Transport: 40 ft reefer container, or air freight for small lots and lychee":
  ("运输方式：40 尺冷藏柜；小批量和荔枝走空运",
   "النقل: حاوية مبرّدة 40 قدماً، أو شحن جوي للدفعات الصغيرة والليتشي"),
"Payment terms": ("付款条件", "شروط الدفع"),
"<b>First order</b> — 30% T/T deposit, balance before B/L release":
  ("<b>首单</b> — 电汇预付 30%，余款在放提单前结清",
   "<b>الطلب الأول</b> — دفعة 30٪ تحويلاً بنكياً والباقي قبل الإفراج عن بوليصة الشحن"),
"<b>Repeat buyers</b> — L/C at sight or 30-day T/T, case by case":
  ("<b>老客户</b> — 即期信用证或 30 天电汇，个案商定",
   "<b>العملاء المتكررون</b> — اعتماد مستندي بالاطلاع أو تحويل خلال 30 يوماً، حسب كل حالة"),
"Quoted in USD or THB · quotations valid 7 days (longan farm-gate prices move weekly)":
  ("以美元或泰铢报价 · 报价有效期 7 天（龙眼田头价每周变动）",
   "التسعير بالدولار أو الباهت · العرض صالح 7 أيام (أسعار اللونجان عند المزرعة تتغير أسبوعياً)"),
"Where we are ready to ship": ("我们已准备好发货的市场", "الوجهات الجاهزون للشحن إليها"),
"China": ("中国", "الصين"),
"Longan, durian, mangosteen · via Youyiguan or sea port · GACC registration required":
  ("龙眼、榴莲、山竹 · 经友谊关或海运口岸 · 需海关总署注册",
   "لونجان ودوريان ومانجوستين · عبر يويي‑قوان أو الموانئ البحرية · يلزم تسجيل GACC"),
"Hong Kong / Singapore": ("香港 / 新加坡", "هونغ كونغ / سنغافورة"),
"Small, frequent lots — well suited to air freight": ("小批量、高频次 — 适合空运", "دفعات صغيرة ومتكررة — مناسبة للشحن الجوي"),
"Europe": ("欧洲", "أوروبا"),
"Netherlands, France · strict on MRL and SO₂ limits":
  ("荷兰、法国 · 对残留限量和二氧化硫要求严格", "هولندا وفرنسا · صارمة في حدود المتبقيات وثاني أكسيد الكبريت"),
"Middle East": ("中东", "الشرق الأوسط"),
"Dubai · gifting and premium supermarket channels": ("迪拜 · 礼品和高端超市渠道", "دبي · قنوات الهدايا والسوبرماركت الفاخر"),

# ---- contact ----
"Reach us": ("联系方式", "تواصل معنا"),
"You will be talking to the people who do the work": ("接电话的就是干活的人", "ستتحدث مع من يقوم بالعمل فعلاً"),
"There is no call centre here. If you have questions about grades, seasons or destination requirements, ask — even if you are not ready to order.":
  ("我们没有客服中心。关于等级、季节或目的地要求有任何疑问都可以问，即使还没打算下单。",
   "لا يوجد مركز اتصال هنا. إن كان لديك سؤال عن الدرجات أو المواسم أو اشتراطات الوجهة فاسأل، حتى إن لم تكن جاهزاً للطلب."),
"LINE and WeChat on the same number": ("LINE 和微信同号", "لاين وويتشات على الرقم نفسه"),
"Packing shed: Mueang District, Lamphun · Office: Bangkok":
  ("分选场：南奔府孟县 · 办公室：曼谷", "محطة التعبئة: مقاطعة موانغ، لامفون · المكتب: بانكوك"),
"Mon–Sat 08:00–17:00 Thailand time · during longan season we are at the shed all day":
  ("周一至周六 08:00–17:00（泰国时间）· 龙眼季我们整天都在分选场",
   "الاثنين–السبت 08:00–17:00 بتوقيت تايلاند · في موسم اللونجان نكون في المحطة طوال اليوم"),
"Send quotation request": ("发送报价请求", "إرسال طلب العرض"),
"Demo form for this draft site — not yet connected to a mail service.":
  ("本草稿网站的示例表单，尚未连接邮件服务。", "نموذج تجريبي لهذه النسخة — غير موصول بخدمة بريد بعد."),
"Full name": ("姓名", "الاسم الكامل"),
"Email": ("电子邮箱", "البريد الإلكتروني"),
"Destination country": ("目的地国家", "بلد الوجهة"),
"Product": ("产品", "المنتج"),
"Incoterm": ("贸易术语", "شرط التسليم"),
"Mixed / several": ("多种混装", "متنوّع / أكثر من صنف"),
"Not sure yet": ("尚未确定", "غير محدد بعد"),
"Approximate volume and timing": ("大致数量和时间", "الكمية التقريبية والتوقيت"),
}

# Month abbreviations for the harvest calendar
MONTHS = {
    "zh": ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"],
    "ar": ["ينا","فبر","مار","أبر","ماي","يون","يول","أغس","سبت","أكت","نوف","ديس"],
}

# <title> and meta description per page
META = {
"index.html": {
  "zh": ("泰国龙眼出口商 | Alpha Fresh，南奔府",
         "Alpha Fresh 出口泰国南奔府人工分级新鲜龙眼，应季另有榴莲、山竹和荔枝。GAP 果园、全程冷链，可做 FOB 与 CIF。"),
  "ar": ("مصدّر اللونجان التايلاندي | ألفا فريش، لامفون",
         "تصدّر ألفا فريش لونجان طازجاً مفروزاً يدوياً من لامفون، إضافة إلى الدوريان والمانجوستين والليتشي موسمياً. بساتين GAP وسلسلة تبريد كاملة، بشروط FOB وCIF."),
},
"about.html": {
  "zh": ("关于 Alpha Fresh — 从进口商到出口商",
         "从水果进口商转为出口商：自有冷库、冷藏车和南奔府的分选场，背后是二十多个 GAP 认证龙眼果园。"),
  "ar": ("عن ألفا فريش — من مستورد إلى مصدّر",
         "من استيراد الفاكهة إلى تصديرها: غرفة تبريد وشاحنة مبرّدة ومحطة تعبئة في لامفون، خلفها أكثر من عشرين بستان لونجان معتمداً بشهادة GAP."),
},
"products.html": {
  "zh": ("龙眼规格、等级与泰国水果产季 | Alpha Fresh",
         "完整龙眼出口规格 — 依多、多、标绿品种，AA 至 C 级，5 与 10 公斤包装，保鲜 21–30 天 — 另附泰国水果产季日历。"),
  "ar": ("مواصفات اللونجان ودرجاته ومواسم الفواكه التايلاندية | ألفا فريش",
         "مواصفة تصدير اللونجان كاملة — أصناف إي‑داو وداو وبيو كيو، درجات AA حتى C، تعبئة 5 و10 كغ، صلاحية 21–30 يوماً — مع روزنامة حصاد الفواكه التايلاندية."),
},
"quality.html": {
  "zh": ("品质、冷链与出口条件 | Alpha Fresh",
         "订单如何进行、GAP GMP 与 HACCP 规范、欧盟中国日本残留检测、全程冷链、Incoterms 2020 及首单付款条件。"),
  "ar": ("الجودة وسلسلة التبريد وشروط التصدير | ألفا فريش",
         "كيف يسير الطلب، وممارسات GAP وGMP وHACCP، وفحص المتبقيات للاتحاد الأوروبي والصين واليابان، وسلسلة تبريد غير منقطعة، وإنكوترمز 2020 وشروط الدفع."),
},
"contact.html": {
  "zh": ("索取龙眼出口报价 | Alpha Fresh",
         "索取泰国新鲜龙眼、榴莲、山竹或荔枝的报价。两个工作日内回复价格与采摘排期，支持 LINE 与微信。"),
  "ar": ("اطلب عرض سعر لتصدير اللونجان | ألفا فريش",
         "اطلب عرض سعر للونجان التايلاندي الطازج أو الدوريان أو المانجوستين أو الليتشي. الرد بالسعر وجدول القطف خلال يومَي عمل، وعبر لاين وويتشات."),
},
# ---- page headers on the inner pages ----
"From importer to exporter": ("从进口商到出口商", "من مستورد إلى مصدّر"),
"We did not start from nothing. The cold room, the refrigerated truck and the customs paperwork were already ours from the import side. What we added is our own packing shed in Lamphun.":
  ("我们不是从零开始。冷库、冷藏车和报关单证在做进口时就已经有了。新增的是南奔府自己的分选包装场。",
   "لم نبدأ من الصفر. غرفة التبريد والشاحنة المبرّدة ومستندات الجمارك كانت لدينا أصلاً من جانب الاستيراد. ما أضفناه هو محطة التعبئة الخاصة بنا في لامفون."),
"Longan, and Thai fruit in season": ("龙眼，以及应季的泰国水果", "اللونجان وفواكه تايلاند في موسمها"),
"Longan is our flagship — the full specification is below. Durian, mangosteen and lychee are taken to order in season, through packing houses we have worked with for years.":
  ("龙眼是我们的主力产品，完整规格见下方。榴莲、山竹和荔枝按应季订单供应，通过多年合作的包装厂组织货源。",
   "اللونجان منتجنا الرئيسي، ومواصفته الكاملة أدناه. أما الدوريان والمانجوستين والليتشي فتُورَّد حسب الطلب في موسمها عبر محطات تعبئة نعمل معها منذ سنوات."),
"Checked, traceable, and delivered in the condition it left":
  ("可查验、可追溯，送到时和出发时一样", "مفحوص وقابل للتتبع ويصل بالحالة التي غادر بها"),
"Everything a buyer usually asks before a first order — how an order runs, the standards we work to, residue testing, the cold chain, and our delivery and payment terms.":
  ("买家在首单前通常会问的一切 — 订单流程、我们遵循的标准、残留检测、冷链，以及交货和付款条件。",
   "كل ما يسأل عنه المشتري عادةً قبل الطلب الأول — سير الطلب، والمعايير التي نلتزم بها، وفحص المتبقيات، وسلسلة التبريد، وشروط التسليم والدفع."),
"Tell us the fruit, the volume and the destination. You will get a price and a picking schedule back within two working days.":
  ("告诉我们水果种类、数量和目的地，我们会在两个工作日内回复价格和采摘排期。",
   "أخبرنا بنوع الفاكهة والكمية والوجهة، وسنرد بالسعر وجدول القطف خلال يومَي عمل."),
}


# Trade jargon explained in plain language, in all four site languages.
# Order: en, th, zh, ar
GLOSSARY = {
"FOB": (
  "Free On Board — our price covers the fruit delivered onto the ship or aircraft at the named Thai port. From that point the buyer pays freight, insurance and everything after.",
  "Free On Board — ราคาของเราครอบคลุมถึงตอนที่ของขึ้นเรือหรือขึ้นเครื่องที่ท่าต้นทางในไทย จากจุดนั้นผู้ซื้อรับผิดชอบค่าระวาง ค่าประกัน และทุกอย่างต่อจากนั้น",
  "船上交货 — 我们的报价含把货交到泰国指定港口装船或装机为止。此后的运费、保险及一切费用由买方承担。",
  "التسليم على ظهر السفينة — يشمل سعرنا تسليم البضاعة على متن السفينة أو الطائرة في الميناء التايلاندي المحدد. بعد ذلك يتحمّل المشتري الشحن والتأمين وكل ما يليهما."),
"CIF": (
  "Cost, Insurance and Freight — our price also covers sea freight and marine insurance all the way to your destination port. Customs clearance at your end is still yours.",
  "Cost, Insurance and Freight — ราคารวมค่าระวางเรือและค่าประกันภัยไปจนถึงท่าปลายทางของคุณ แต่พิธีการขาเข้าที่ปลายทางยังเป็นของผู้ซื้อ",
  "成本加保险费加运费 — 报价另含海运费和海运保险，直至您的目的港。目的港清关仍由买方负责。",
  "التكلفة والتأمين والشحن — يشمل سعرنا أيضاً الشحن البحري والتأمين حتى ميناء وجهتكم. أما التخليص الجمركي عندكم فيبقى على عاتقكم."),
"CFR": (
  "Cost and Freight — the same as CIF but without the insurance; you arrange cover yourself.",
  "Cost and Freight — เหมือน CIF แต่ไม่รวมค่าประกันภัย ผู้ซื้อทำประกันเอง",
  "成本加运费 — 与 CIF 相同，但不含保险，由买方自行投保。",
  "التكلفة والشحن — مثل CIF لكن دون تأمين؛ تتولون التأمين بأنفسكم."),
"EXW": (
  "Ex Works — you collect from our packing shed in Lamphun and carry every cost from the gate onward. The cheapest headline price, the most work for the buyer.",
  "Ex Works — ผู้ซื้อมารับของเองที่โรงคัดของเราที่ลำพูน และรับผิดชอบค่าใช้จ่ายทั้งหมดตั้งแต่หน้าประตู ราคาหน้าตาถูกที่สุด แต่ผู้ซื้อเหนื่อยที่สุด",
  "工厂交货 — 买方到我们南奔府的分选场自提，出厂后的一切费用自理。报价最低，但买方工作量最大。",
  "التسليم في المصنع — تستلمون من محطتنا في لامفون وتتحملون كل التكاليف من البوابة فصاعداً. أقل سعر معلن، وأكبر عبء على المشتري."),
"Incoterms 2020": (
  "The International Chamber of Commerce's standard trade terms. They settle one question: at which exact point do cost and risk pass from seller to buyer.",
  "ข้อกำหนดทางการค้ามาตรฐานของหอการค้านานาชาติ ตอบคำถามเดียวคือ ค่าใช้จ่ายและความเสี่ยงเปลี่ยนมือจากผู้ขายไปผู้ซื้อตรงจุดไหน",
  "国际商会制定的标准贸易术语，只解决一个问题：费用和风险在哪一点从卖方转移到买方。",
  "الشروط التجارية المعيارية لغرفة التجارة الدولية. تحسم سؤالاً واحداً: عند أي نقطة بالضبط تنتقل التكلفة والمخاطرة من البائع إلى المشتري."),
"GACC": (
  "General Administration of Customs of China. Fruit may only enter China from orchards and packing houses registered on its list — no registration, no shipment.",
  "สำนักงานศุลกากรแห่งสาธารณรัฐประชาชนจีน ผลไม้จะเข้าจีนได้เฉพาะจากสวนและโรงคัดที่ขึ้นทะเบียนกับ GACC เท่านั้น ไม่มีทะเบียน = ส่งไม่ได้",
  "中华人民共和国海关总署。水果只能来自在其名单上注册的果园和包装厂才可输华 — 未注册即不可出运。",
  "الإدارة العامة للجمارك الصينية. لا تدخل الفاكهة الصين إلا من بساتين ومحطات تعبئة مسجّلة لديها — بلا تسجيل لا شحن."),
"MRL": (
  "Maximum Residue Limit — the highest amount of a given pesticide the destination country allows on the fruit. Exceed it and the shipment is rejected at the border.",
  "ค่าปริมาณสารตกค้างสูงสุดที่ประเทศปลายทางยอมให้มีในผลไม้ ถ้าเกินค่านี้ สินค้าจะถูกปฏิเสธที่ด่าน",
  "最大残留限量 — 目的地国家允许水果上残留某种农药的最高值。超标即在口岸被拒收。",
  "الحد الأقصى للمتبقيات — أعلى كمية مسموح بها من مبيد معيّن على الفاكهة في بلد الوجهة. وتجاوزه يعني رفض الشحنة على الحدود."),
"GAP": (
  "Good Agricultural Practice — farm-level certification covering how pesticides are used and recorded, water quality, and worker hygiene.",
  "การปฏิบัติทางการเกษตรที่ดี — มาตรฐานระดับสวน ครอบคลุมการใช้และบันทึกสารเคมี คุณภาพน้ำ และสุขอนามัยของคนงาน",
  "良好农业规范 — 果园层面的认证，涵盖农药使用与记录、水质和工人卫生。",
  "الممارسات الزراعية الجيدة — شهادة على مستوى المزرعة تغطي استخدام المبيدات وتوثيقها وجودة المياه ونظافة العاملين."),
"GMP": (
  "Good Manufacturing Practice — the hygiene and process rules a packing house follows: layout, cleaning, staff clothing, record keeping.",
  "หลักเกณฑ์วิธีการที่ดีในการผลิต — กฎด้านสุขอนามัยและกระบวนการของโรงคัด ทั้งผังโรงงาน การทำความสะอาด ชุดพนักงาน และการบันทึก",
  "良好生产规范 — 包装厂遵循的卫生与流程规则：布局、清洁、员工着装、记录留存。",
  "ممارسات التصنيع الجيدة — قواعد النظافة والعمليات التي تتبعها محطة التعبئة: التخطيط والتنظيف وملابس العاملين وحفظ السجلات."),
"HACCP": (
  "Hazard Analysis and Critical Control Points — a food-safety method that maps where contamination could happen and puts a check at each of those points.",
  "การวิเคราะห์อันตรายและจุดวิกฤตที่ต้องควบคุม — ระบบความปลอดภัยอาหารที่ไล่หาจุดที่อาจปนเปื้อน แล้ววางจุดตรวจไว้ทุกจุดนั้น",
  "危害分析与关键控制点 — 一套食品安全方法，找出可能发生污染的环节并在每个环节设置管控。",
  "تحليل المخاطر ونقاط التحكم الحرجة — منهج لسلامة الغذاء يحدد مواضع التلوث المحتملة ويضع نقطة ضبط عند كل منها."),
"Phytosanitary": (
  "A government certificate, issued per shipment, stating the fruit was inspected and is free of pests the importing country bars.",
  "ใบรับรองสุขอนามัยพืชที่ออกโดยราชการ ออกให้ทีละชิปเมนต์ ระบุว่าผลไม้ผ่านการตรวจและปลอดศัตรูพืชที่ประเทศปลายทางห้าม",
  "植物检疫证书 — 由政府逐批签发，证明水果已经检验且不带进口国禁止的有害生物。",
  "شهادة صحة نباتية حكومية تُصدر لكل شحنة، تفيد بأن الفاكهة فُحصت وخالية من الآفات التي يمنعها بلد الاستيراد."),
"T/T": (
  "Telegraphic Transfer — an ordinary bank wire. Fast and cheap, but it offers the buyer no bank guarantee.",
  "การโอนเงินผ่านธนาคาร — เร็วและค่าธรรมเนียมถูก แต่ผู้ซื้อไม่ได้รับการค้ำประกันจากธนาคาร",
  "电汇 — 普通银行汇款，快且便宜，但买方得不到银行担保。",
  "تحويل بنكي — سريع ومنخفض التكلفة، لكنه لا يمنح المشتري ضماناً مصرفياً."),
"L/C": (
  "Letter of Credit — the buyer's bank promises to pay once the shipping documents match the agreed terms exactly. Safer for both sides, slower and more expensive.",
  "เลตเตอร์ออฟเครดิต — ธนาคารของผู้ซื้อรับประกันการจ่ายเงินเมื่อเอกสารการส่งออกตรงตามเงื่อนไขทุกข้อ ปลอดภัยกับทั้งสองฝ่าย แต่ช้ากว่าและค่าธรรมเนียมสูงกว่า",
  "信用证 — 买方银行承诺，只要单据与约定条款完全相符即付款。对双方都更安全，但更慢、费用更高。",
  "الاعتماد المستندي — يتعهّد بنك المشتري بالدفع متى طابقت مستندات الشحن الشروط المتفق عليها تماماً. أأمن للطرفين، لكنه أبطأ وأعلى كلفة."),
"B/L": (
  "Bill of Lading — the sea carrier's document. Whoever holds the original controls the cargo, which is why it is released only against payment.",
  "ใบตราส่งสินค้าทางทะเล — ใครถือต้นฉบับคนนั้นคุมสินค้า จึงปล่อยให้ต่อเมื่อชำระเงินแล้ว",
  "海运提单 — 承运人签发的单据。谁持有正本谁就控制货物，因此凭付款才放单。",
  "بوليصة الشحن البحري — وثيقة الناقل. من يحمل الأصل يتحكم بالبضاعة، ولذلك لا تُسلَّم إلا مقابل الدفع."),
"AWB": (
  "Air Waybill — the air freight version of a bill of lading. Unlike a B/L it is not a document of title, so payment terms are handled differently.",
  "ใบตราส่งสินค้าทางอากาศ — เทียบเท่า B/L ของการขนส่งทางอากาศ แต่ไม่ใช่เอกสารแสดงกรรมสิทธิ์ เงื่อนไขการชำระเงินจึงต่างออกไป",
  "空运单 — 空运版的提单。与海运提单不同，它不是物权凭证，因此付款条件处理方式不同。",
  "بوليصة الشحن الجوي — نظير بوليصة الشحن البحري في النقل الجوي. لكنها ليست وثيقة ملكية، لذا تُعالَج شروط الدفع بطريقة مختلفة."),
}
