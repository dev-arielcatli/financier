export type Income = Readonly<{
  id: string;
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: Date;
  createdAt: Date;
  updatedAt: Date;
  address: string;
  sources: string[];
  tags: string[];
}>;

export type SafeDisplayIncome = Readonly<{
  id: string;
  name: string;
  description: string;
  quantity: number;
  amount: number;
  date: string;
  createdAt: string;
  updatedAt: string;
  address: string;
  // TODO: Forms have issues with this model
  sources: any;
  tags: any;
}>;
