# ユーザー登録イベントの概要

ユーザー登録イベントは、アプリケーションの新規ユーザー登録プロセスの方法を示します。この仕様は、イベントパターン、属性、発生条件について説明しています。

## イベントの目的

ユーザー登録イベントは、システムに新しいユーザーが追加されたことをトラッキングし、ログイン統計やマーケティングツールに送信するために使用されます。

## イベントの属性

| 属性名           | 型       | 必須 | 説明                     |
|-----------------|----------|------|-------------------------|
| `user_id`        | string   | はい | 一意のユーザー識別子      |
| `registration_time` | datetime | はい | 登録日時（ISO 8601形式）  |
| `signup_method`  | string   | いいえ | 登録に使用された方法（例：Google, Email） |

## 発生シナリオ

このイベントは、ユーザーが「登録」ボタンを押した直後に発生します。以下の場合には発生しません：

- ゲストログイン時
- 既存ユーザーの再登録時

## 注意事項

- `registration_time` はサーバー側で記録され、クライアントによる改ざんを防止します。
- `signup_method` がない場合は、「Unknown」として処理されます。

## 参照

詳細は [ユーザー登録APIドキュメント](https://example.com/api/user-registration) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->