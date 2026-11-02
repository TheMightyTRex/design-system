/*
 * Board helper for the Storyarr area boards (not part of the library).
 * - [data-phone="query"] boxes get an iframe of this same page at 390px, so the phone preview uses the
 *   library's real phone styles. Inside the frame, everything marked [data-board] is removed.
 * - ?open=<layer id> opens that slide-out, ?dialog=<id> opens that dialog, ?at=<id> scrolls to it.
 * - [data-view] blocks switch with radios that have data-show-view, or with ?view=<name>.
 */
(() => {
  const params = new URLSearchParams(location.search);
  const framed = window.self !== window.top;
  const showView = (name) =>
    document.querySelectorAll("[data-view]").forEach((el) => {
      el.hidden = el.dataset.view !== name;
    });
  document.addEventListener("DOMContentLoaded", () => {
    if (framed) document.querySelectorAll("[data-board]").forEach((el) => el.remove());
    document.querySelectorAll("input[data-show-view]").forEach((input) => {
      input.addEventListener("change", () => input.checked && showView(input.dataset.showView));
      if (params.get("view") === input.dataset.showView) input.checked = true;
    });
    if (params.get("view")) showView(params.get("view"));
    const at = params.get("at");
    if (at) document.getElementById(at)?.scrollIntoView();
    setTimeout(() => {
      const open = params.get("open");
      if (open) window.SharedComponents?.openLayer(open);
      const dlg = params.get("dialog");
      if (dlg) document.getElementById(dlg)?.showModal();
    }, 30);
    if (!framed)
      document.querySelectorAll("[data-phone]").forEach((box) => {
        const frame = document.createElement("iframe");
        frame.src = `${location.pathname}?${box.dataset.phone}`;
        frame.title = box.dataset.title || "Phone preview";
        frame.width = "390";
        frame.height = box.dataset.height || "760";
        frame.style.border = "0";
        frame.style.display = "block";
        box.append(frame);
      });
  });
})();
