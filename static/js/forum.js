document.addEventListener("DOMContentLoaded",function(){
    let comments_tag = document.getElementById("comments-tag")
    let commentsList = JSON.parse(comments_tag.innerHTML.split("").map(x=> x=="'"?'"':x).join(""))
    let commentContainer = document.getElementById("comment-container")
    let newCommentString=""
    for(let i=0;i<commentsList.length;i++){
        let newComment = `${commentsList[i]}<br></br>`
        newCommentString=newCommentString+newComment
    }
    commentContainer.innerHTML = commentContainer.innerHTML+newCommentString
})