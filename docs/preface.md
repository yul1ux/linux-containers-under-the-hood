# Preface

Docker ဒါမှမဟုတ် Podman ကို သုံးပြီး container တစ်ခု run လုပ်ရတာ မခက်ပါဘူး။ Command ကို သိထားရင် application ကို စတင်နိုင်ပါတယ်။ ဒါပေမဲ့ container တစ်ခု run နေတဲ့အချိန်မှာ အောက်ခံမှာ ဘာတွေဖြစ်နေလဲဆိုတာကိုတော့ command သိရုံနဲ့ မရှင်းပြနိုင်သေးပါဘူး။

ဥပမာ container ထဲက process တွေကို Linux က ဘယ်လိုခွဲခြားထားသလဲ။ Container တစ်ခုက ကိုယ့် filesystem ကိုပဲ မြင်နေရတာ ဘာကြောင့်လဲ။ Memory limit သတ်မှတ်လိုက်တဲ့အခါ kernel က ဘယ်လိုထိန်းချုပ်သလဲ။ Image တစ်ခုကို run လုပ်တဲ့အခါ runtime က ဘာတွေပြင်ဆင်ပေးရသလဲ။ ဒီလိုမေးခွန်းတွေကို ဖြေဖို့ဆိုရင် container ကို သုံးနည်းတင်မကဘဲ အလုပ်လုပ်ပုံကိုပါ နားလည်ဖို့ လိုပါတယ်။

ဒီစာအုပ်ကို အဲဒီအကြောင်းတွေကို အခြေခံကနေ စပြီး တစ်ဆင့်ချင်း လေ့လာနိုင်ဖို့ ရေးထားပါတယ်။ Container ကို command တစ်ခု ဒါမှမဟုတ် image file တစ်ခုအဖြစ်ပဲ မကြည့်ဘဲ Linux kernel က စီမံပေးနေတဲ့ process တွေ၊ သူတို့မြင်ရတဲ့ resource တွေနဲ့ runtime က ပြင်ဆင်ပေးတဲ့ execution environment တစ်ခုအဖြစ် ကြည့်သွားပါမယ်။

## ဘယ်သူတွေ ဖတ်လို့ရမလဲ

Linux နဲ့ container နည်းပညာကို ပိုနားလည်ချင်သူတွေအတွက် ဒီစာအုပ်ကို ရည်ရွယ်ထားပါတယ်။ ဥပမာ—

- Linux ကို စတင်လေ့လာနေပြီး process နဲ့ kernel အလုပ်လုပ်ပုံကို ပိုသိချင်သူများ။
- Docker၊ Podman ဒါမှမဟုတ် အခြား container tool တွေကို နေ့စဉ်သုံးနေရပေမဲ့ နောက်ကွယ်က mechanism တွေကို သိချင်သူများ။
- System administration၊ DevOps၊ Site Reliability Engineering (SRE) နဲ့ platform engineering နယ်ပယ်တွေမှာ လုပ်ကိုင်နေသူများ။
- Linux process၊ namespace၊ cgroup၊ filesystem နဲ့ container runtime architecture တို့ကို ပိုနက်နက်ရှိုင်းရှိုင်း လေ့လာချင်သူများ။

Docker၊ Podman၊ Kubernetes ဒါမှမဟုတ် OCI specification တွေကို ကြိုသိထားဖို့ မလိုပါဘူး။ Linux terminal ကို အခြေခံအသုံးပြုဖူးပြီး file၊ directory၊ process ဆိုတာတွေကို အကြမ်းဖျဉ်း သိထားရင် စတင်ဖတ်လို့ရပါတယ်။ ဘယ်လောက်အထိ ကြိုသိထားဖို့ လိုသလဲဆိုတာကို [Before You Begin](before-you-begin.md) မှာ ပိုရှင်းပြထားပါတယ်။

## ဘာတွေကို လေ့လာသွားမလဲ

စာအုပ်ရဲ့ အဓိကအာရုံစိုက်ရာက Linux OS-level container တွေနဲ့ အဲဒီ container တွေကို ဖြစ်လာစေတဲ့ kernel၊ userspace mechanism တွေပါ။ အကြောင်းအရာတွေကို အပိုင်း ၆ ပိုင်းခွဲထားပါတယ်။

1. **Part I — Container Fundamentals:** Container ရဲ့ အခြေခံသဘောတရား၊ Virtual Machine နဲ့ ကွာခြားချက်၊ Linux process နဲ့ system call တွေကို စလေ့လာမယ်။
2. **Part II — Linux Kernel and Isolation:** Namespace၊ control group၊ capability နဲ့ filesystem isolation တို့ကို ပိုအသေးစိတ် ကြည့်မယ်။
3. **Part III — Filesystem and Networking:** OverlayFS၊ container image storage နဲ့ network အတွင်းပိုင်းကို လေ့လာမယ်။
4. **Part IV — OCI and Container Runtime Internals:** OCI specification၊ `runc`၊ `crun`၊ `containerd`၊ `containerd-shim` နဲ့ Docker Engine တို့ရဲ့ အခန်းကဏ္ဍကို ခွဲကြည့်မယ်။
5. **Part V — Security and Operations:** Container security mechanism တွေ၊ rootless container နဲ့ လုပ်ငန်းလည်ပတ်ရာမှာ ကြုံနိုင်တဲ့ ပြဿနာတွေကို လေ့လာမယ်။
6. **Part VI — Ecosystem and Capstone:** Podman၊ Kubernetes runtime architecture နဲ့ ကိုယ်ပိုင် Linux container runtime တစ်ခု တည်ဆောက်လေ့လာခြင်းအထိ သွားမယ်။

အပိုင်းတစ်ခုချင်းစီဟာ အရင်အပိုင်းမှာ သိခဲ့တာတွေကို အခြေခံပြီး နောက်တစ်ဆင့် တိုးသွားအောင် စီစဉ်ထားပါတယ်။ ဒါပေမဲ့ Docker၊ Podman နဲ့ Kubernetes တို့ရဲ့ implementation အားလုံး တူညီတယ်လို့ မဆိုလိုပါဘူး။ သက်ဆိုင်ရာ specification က သတ်မှတ်ထားတဲ့ behavior၊ Linux kernel ရဲ့ behavior နဲ့ tool တစ်ခုချင်းစီရဲ့ implementation ကို လိုအပ်သလို ခွဲပြီး ရှင်းပြပါမယ်။

## ရှင်းပြပုံ

အကြောင်းအရာတစ်ခုကို အရင်ဆုံး ဘာကြောင့် လိုအပ်လာသလဲဆိုတာကနေ စပါမယ်။ ပြီးရင် ဥပမာနဲ့ စိတ်ကူးကြည့်ပြီး technical term၊ အလုပ်လုပ်ပုံနဲ့ အခြား mechanism တွေနဲ့ ဆက်စပ်ပုံကို ရှင်းပြပါမယ်။ လိုအပ်တဲ့နေရာမှာ table၊ diagram၊ command နဲ့ code snippet တွေကို ထည့်သုံးထားပါတယ်။

Command၊ system call၊ API၊ file path နဲ့ specification အမည်တွေကို မူရင်း English အတိုင်း ထားပါတယ်။ ဒီလိုထားတာက documentation တွေမှာ ပြန်ရှာတဲ့အခါ ပိုလွယ်စေဖို့ပါ။ အဲဒီ term တွေကို ပထမဆုံးတွေ့တဲ့နေရာမှာ မြန်မာလို ရှင်းပြပေးထားပါတယ်။

နောက်တစ်ခုက version နဲ့ implementation ကွာခြားချက်ပါ။ Linux kernel version တစ်ခုနဲ့ တစ်ခု၊ runtime တစ်ခုနဲ့ တစ်ခု၊ Docker နဲ့ Podman တို့မှာ အပြုအမူတချို့ ကွာနိုင်ပါတယ်။ ဒါကြောင့် အားလုံးမှာ အမြဲတူတယ်လို့ မရေးဘဲ ဘယ်အခြေအနေမှာ မှန်သလဲဆိုတာကို ရှင်းလင်းဖော်ပြဖို့ ကြိုးစားထားပါတယ်။

## Lab တွေအကြောင်း

စာအုပ်ထဲက Lab တွေက ဖတ်ထားတဲ့ concept ကို ကိုယ်တိုင်ကြည့်ပြီး နားလည်စေဖို့ ရည်ရွယ်ပါတယ်။ Lab တစ်ခုချင်းစီမှာ လိုအပ်ချက်၊ လုပ်ဆောင်ပုံ၊ မျှော်မှန်းထားတဲ့ observation၊ ရလဒ်ကို ဘယ်လိုဖတ်ရမလဲ၊ ပြဿနာဖြစ်ရင် ဘာစစ်ရမလဲနဲ့ cleanup ကို ဖော်ပြသွားပါမယ်။

ဒါပေမဲ့ Lab instruction ရှိတာနဲ့ လက်တွေ့စမ်းသပ်ပြီးပြီလို့ မယူဆပါနဲ့။ စမ်းသပ်ပြီး/မပြီး status ကို သက်ဆိုင်ရာ Lab မှာ ထည့်ရေးထားပါမယ်။ Privilege လိုအပ်တဲ့ command၊ host setting ပြောင်းတဲ့အလုပ် ဒါမှမဟုတ် production system ပေါ်က စမ်းသပ်မှုတွေကို ခွင့်ပြုချက်မရှိဘဲ မလုပ်သင့်ပါဘူး။

## စာဖတ်သူအတွက်

ဒီစာအုပ်ကို အစကနေ အဆုံးထိ တစ်ခါတည်း ဖတ်ဖို့ မလိုပါဘူး။ အခန်းတွေကို အစဉ်လိုက် ဖတ်ရင် အကြောင်းအရာတွေ ပိုဆက်စပ်နားလည်နိုင်ပါတယ်။ တစ်ခုခု မရှင်းရင် အဲဒီအခန်းရဲ့ diagram၊ ဥပမာနဲ့ reference ကို ပြန်ကြည့်ပါ။ Technical term တစ်ခုကို နားလည်သွားတာထက် အဲဒါက ဘာပြဿနာကို ဖြေရှင်းပေးတာလဲ၊ ဘယ်အရာတွေကို မဖြေရှင်းပေးနိုင်ဘူးလဲဆိုတာကိုပါ စဉ်းစားကြည့်ပါ။

Container တစ်ခုကို run လုပ်တတ်တာက စတင်ခြင်းပါ။ ဘာကြောင့် အဲဒီလို run နေသလဲဆိုတာကို ရှင်းပြနိုင်လာတာက ဒီစာအုပ်က ကူညီချင်တဲ့ နောက်တစ်ဆင့် ဖြစ်ပါတယ်။
