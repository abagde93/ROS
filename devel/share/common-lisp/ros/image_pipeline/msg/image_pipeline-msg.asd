
(cl:in-package :asdf)

(defsystem "image_pipeline-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Floats" :depends-on ("_package_Floats"))
    (:file "_package_Floats" :depends-on ("_package"))
  ))