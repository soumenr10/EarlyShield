// Fix: expose initFieldReport as proper scope and fix upload zone
(function(){
  // Fix initFieldReport scope for upload zone + file input
  var uploadZone = document.getElementById("upload-zone");
  var fileInput = document.getElementById("file-input");
  if(uploadZone && fileInput){
    uploadZone.addEventListener("dragover", function(e){e.preventDefault();uploadZone.classList.add("dragover")});
    uploadZone.addEventListener("dragleave", function(){uploadZone.classList.remove("dragover")});
    uploadZone.addEventListener("drop", function(e){
      e.preventDefault(); uploadZone.classList.remove("dragover");
      var files = e.dataTransfer.files;
      if(!files||!files.length)return;
      var names = Array.from(files).map(function(f){return f.name}).join(", ");
      showToast("success","Files Selected",files.length+" file(s): "+names,3000);
      uploadZone.innerHTML = "<div class='upload-icon'>&#10003;</div><p style='color:#27ae60;font-weight:700'>"+files.length+" file(s) ready</p><p style='font-size:.8rem;color:var(--text-muted)'>"+names+"</p>";
    });
    uploadZone.addEventListener("click", function(){fileInput.click()});
    fileInput.addEventListener("change", function(e){
      var files = e.target.files;
      if(!files||!files.length)return;
      var names = Array.from(files).map(function(f){return f.name}).join(", ");
      showToast("success","Files Selected",files.length+" file(s): "+names,3000);
      uploadZone.innerHTML = "<div class='upload-icon'>&#10003;</div><p style='color:#27ae60;font-weight:700'>"+files.length+" file(s) ready</p><p style='font-size:.8rem;color:var(--text-muted)'>"+names+"</p>";
    });
  }
})();
