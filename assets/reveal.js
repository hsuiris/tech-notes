/* 捲到畫面裡才讓區塊浮出來。
   系統開了「減少動態效果」就整個不做，內容維持原樣直接顯示。 */
(function () {
  if (matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  if (!("IntersectionObserver" in window)) return;

  var els = document.querySelectorAll(
    ".card,.rel,.job,.step,.chain,.term,.lg,.skip,.fig,.callout,.tools"
  );
  if (!els.length) return;

  document.documentElement.classList.add("reveal-on");
  els.forEach(function (el) { el.classList.add("rv"); });

  var fired = false;
  var io = new IntersectionObserver(function (rows) {
    rows.forEach(function (r) {
      if (!r.isIntersecting) return;
      fired = true;
      r.target.classList.add("rv-in");
      io.unobserve(r.target);
    });
  }, { rootMargin: "0px 0px -6% 0px", threshold: 0.04 });

  els.forEach(function (el) { io.observe(el); });

  // 保險：萬一觀察器一次都沒回報，把全部顯示出來，
  // 寧可沒有動畫，也不能讓內容留在看不見的狀態。
  setTimeout(function () {
    if (fired) return;
    els.forEach(function (el) { el.classList.add("rv-in"); });
  }, 2500);
})();
