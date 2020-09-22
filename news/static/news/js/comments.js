const csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;

// Загрузка комментариев после загрузки страницы
document.addEventListener("DOMContentLoaded", function () {
  get_all_comments();
});

// Получение комментариев
async function get_all_comments() {
  // Запрос
  let response = await fetch(get_comments);
  await response.json().then((data) => {
    let commentsListAll = document.getElementById("comments");
    // Проверка наличия комментариев
    if (data.length === 0) {
      commentsListAll.innerHTML =
        "<div class='card-body d-flex'><p class='card-text mx-auto'>Нет комментариев</p></div>";
    } else {
      // Рендер комментариев
      commentsListAll.innerHTML = "";
      for (var i = 0; i < data.length; i++) {
        let commentsList = document.createElement("div");
        commentsList.classList.add("card-body");
        commentsList.innerHTML = `<small class='mx-auto text-muted'>${data[i].comment_date}</small>
        <button class='btn btn-danger btn-sm float-right' onclick='delete_comment(${data[i].id})'>Удалить</button>
        <p class='card-text mt-3'>${data[i].comment_text}</p>`;
        commentsListAll.appendChild(commentsList);
      }
    }
  });
}

// Добавить комментарий
async function add_comment() {
  let text = document.getElementById("text").value;
  // Валидация формы
  if (text) {
    //   Запрос
    await fetch(add_cmm, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "X-CSRFToken": csrftoken,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(text),
    });
    document.getElementById("text").value = "";
    // Получение обновленного списка комментариев
    get_all_comments();
  }
}

// Удалить комментарий
async function delete_comment(id) {
  let comment_id = id + "/";
  let url = "/api/del_comment/" + post_id + comment_id;
  await fetch(url, {
    method: "POST",
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": csrftoken,
    },
  });
  // Получение обновленного списка комментариев
  get_all_comments();
}
