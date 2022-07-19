
#' Chech path
#'
#'
path_check <- function(path) {
  folders <- stringr::str_split(path, pattern = "\\/")

  root <- "."

  folders <- unlist(folders)

  purrr::walk(folders, function(.x){
    pos <- match(.x, folders)

    #print(pos)

    sub_folder <- paste0(c(root, folders[1:pos]), collapse = "/")

    #print(dir)

    print(paste0(pos, ": ", sub_folder))

    if (!dir.exists(sub_folder)) {
      dir.create(sub_folder)
    }
  })

  dir.exists(path)
}
