# Linux Containers Under the Hood

`docker run` (သို့) `podman run` နဲ့ container တစ်ခု စတင်ဖူးလား။ Command ရိုက်လိုက်တာနဲ့ application က အလုပ်လုပ်သွားပေမဲ့ နောက်ကွယ်မှာ ဘာတွေဖြစ်နေလဲ စဉ်းစားကြည့်ဖူးလား။

- Process တွေကို ဘယ်သူက စီမံပေးနေသလဲ။
- Container တစ်ခုက host ရဲ့ filesystem ကို ဘယ်လိုမြင်သလဲ။
- Memory နဲ့ CPU ကို ဘယ်လို ကန့်သတ်ထားသလဲ။
- Image နဲ့ runtime က ဘာကွာသလဲ။

ဒီစာအုပ်က အဲဒီမေးခွန်းတွေကို မြန်မာဘာသာနဲ့ တစ်ခုချင်း လိုက်ဖြေသွားပါမယ်။ Docker၊ Podman command တွေကို သုံးနည်းပြရုံတင်မကဘဲ အောက်ခံ Linux kernel၊ process၊ filesystem၊ networking နဲ့ runtime တွေ ဘယ်လိုအလုပ်လုပ်သလဲဆိုတာအထိ ကြည့်သွားပါမယ်။

## ဒီစာအုပ်မှာ ဘာတွေပါသလဲ

စာအုပ်ကို Part ၆ ပိုင်း၊ Chapter ၁၉ ခန်းနဲ့ ဖွဲ့ထားပါတယ်။ အခြေခံအယူအဆကနေ kernel mechanism တွေဆီ၊ အဲဒီကနေ runtime နဲ့ ecosystem ဆီ တစ်ဆင့်ချင်း သွားပါမယ်။

| အပိုင်း | ဖြေမယ့်မေးခွန်းများ | Chapter |
|---|---|---:|
| Part I — Container Fundamentals | Container ဆိုတာ ဘာလဲ၊ VM နဲ့ ဘာကွာသလဲ၊ Linux process နဲ့ system call တွေက container နဲ့ ဘယ်လိုဆက်စပ်သလဲ | 1–2 |
| Part II — Linux Kernel and Isolation | Container တစ်ခုကို namespace၊ cgroup၊ capability နဲ့ filesystem isolation တို့က ဘယ်လို ကန့်သတ်ထားသလဲ | 3–6 |
| Part III — Filesystem and Networking | Image layer တွေကို ဘယ်လိုသိမ်းသလဲ (OverlayFS)၊ container တွေ network ကို ဘယ်လိုချိတ်သလဲ | 7–8 |
| Part IV — OCI and Container Runtime Internals | OCI specification၊ `runc`၊ `crun`၊ `containerd` နဲ့ Docker Engine တို့က `docker run` နောက်ကွယ်မှာ ဘယ်လိုပူးပေါင်းလုပ်ဆောင်သလဲ | 9–13 |
| Part V — Security and Operations | Container security mechanism တွေ၊ rootless container နဲ့ troubleshooting | 14–16 |
| Part VI — Ecosystem and Capstone | Podman၊ Kubernetes runtime architecture နဲ့ ကိုယ်ပိုင် Linux container runtime တည်ဆောက်ခြင်း | 17–19 |

## လက်ရှိအခြေအနေ

စာအုပ်ကို အခန်းလိုက် ရေးသားနေဆဲ ဖြစ်ပါတယ်။ **Status snapshot — 18 November 2026**

| Chapter | အခြေအနေ |
|---|---|
| [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md) | Manuscript |
| [Chapter 02 — Linux Processes and System Calls](part-01-fundamentals/chapter-02-linux-processes-and-system-calls.md) | Manuscript |
| [Chapter 03 — Linux Namespaces](part-02-kernel-isolation/chapter-03-linux-namespaces.md) | Working manuscript |
| Chapter 04–19 | စီစဉ်ထားဆဲ (navigation ထဲမှာ ခေါင်းစဉ်ပဲ ရှိသေးတယ်) |

Navigation ထဲမှာ ခေါင်းစဉ်ရှိနေတာက အဲဒီအခန်းရဲ့ စာမူ ပြီးပြီလို့ မဆိုလိုပါဘူး။ Glossary၊ References နဲ့ Appendices ကိုလည်း နောက်မှ ဖြည့်ပါမယ်။ စာမူပြီးတဲ့ အခန်းတွေမှာ ကိုးကားရင်းမြစ်တွေကို အခန်းအဆုံးမှာ ထည့်ထားပါတယ်။

**Lab တွေကို စမ်းသပ်ပြီးသားလို့ မယူဆပါနဲ့။** Chapter 01–03 ရဲ့ Lab တွေက လက်ရှိမှာ **Designed, not tested** ဖြစ်ပါတယ်။ အသေးစိတ်ကို [Before You Begin](before-you-begin.md) မှာ ဖတ်ပါ။

## ဘယ်ကနေ စဖတ်ရမလဲ

1. [Preface](preface.md) — ဒီစာအုပ်ကို ဘာကြောင့်ရေးသလဲ၊ ဘယ်သူတွေအတွက်လဲ၊ ဘယ်လိုရှင်းပြထားသလဲ။
2. [Before You Begin](before-you-begin.md) — ကြိုသိထားရင် ကောင်းတာတွေ၊ ကိုယ့် environment နဲ့ Lab လုံခြုံရေး။
3. [Chapter 01 — Understanding Containers](part-01-fundamentals/chapter-01-understanding-containers.md) ကနေ စတင်ပါ။

အခန်းတွေကို အစဉ်လိုက် ဖတ်ဖို့ အကြံပြုပါတယ်။ နောက်ပိုင်းမှာ တွေ့မယ့် namespace၊ cgroup နဲ့ runtime အကြောင်းတွေက အရင်အခန်းတွေက process နဲ့ kernel အခြေခံပေါ်မှာ တည်ဆောက်ထားလို့ပါ။

## အမှားတွေ့ရင်

အမှားတွေ့ရင် [GitHub repository](https://github.com/yul1ux/linux-containers-under-the-hood) မှာ issue ဖွင့်နိုင်ပါတယ်။ Template ၄ မျိုး ရှိပါတယ် (technical correction၊ Burmese editorial correction၊ documentation defect၊ lab feedback)။ Technical correction မှာ official/versioned source ကို ထည့်ပေးပါ။ Lab feedback ကိုတော့ သီးခြားခွင့်ပြုထားတဲ့အခါမှသာ လက်ခံပါတယ်။ အသေးစိတ်ကို [CONTRIBUTING.md](https://github.com/yul1ux/linux-containers-under-the-hood/blob/main/CONTRIBUTING.md) မှာ ကြည့်ပါ။

စာနဲ့ original diagram တွေက CC BY 4.0၊ original code နဲ့ lab script တွေက MIT licence ဖြစ်ပါတယ်။
